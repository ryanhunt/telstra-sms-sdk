"""
Telstra SMS SDK

Australian Telstra SMS send utility. To access and use this service, sign up for the required API keys at https://dev.telstra.com/

Original code by https://github.com/arkilis
Updated to work with Python 3.4 (latest on Rasbian)

2016, 2017
License: MIT
"""

__version__ = "0.0.7"

import requests
from requests import RequestException
import json

REQUEST_TOKEN_URL = "https://api.telstra.com/v1/oauth/token"
REQUEST_MSG_URL = "https://api.telstra.com/v1/sms/messages"
QUOTA_URL = "https://api.telstra.com/v1/sms/quota"

MSG_TEMPLATE = "G'Day you bonza fellas."


class TelstraSMS(object):
	"""This class helps setting up the client ID, client secret key

	"""

	client_id = None
	client_secret = None
	token = None

	def __init__(self, client_id, client_secret):
		self.client_id = client_id
		self.client_secret = client_secret
		
		self.get_token()

	def get_token(self):
		""" get the token from client id and client secret
		:return: string type of token
		"""
		if self.client_id is None or self.client_secret is None:
			return "Invalid client ID or client secret key"

		# get token
		token_params = {
			'client_id': self.client_id,
			'client_secret': self.client_secret,
			'grant_type': 'client_credentials',
			'scope': 'SMS',
		}

		try:
			r = requests.post(REQUEST_TOKEN_URL, data=token_params)
			try:
				self.token = json.loads(r.text)['access_token']
				return json.loads(r.text)['access_token']
			except TypeError as e:
				print(str(e))
				pass
		except RequestException as e:
			print(str(e))
			pass
		else:
			return None

	def send_sms(self, num, sms_text="Hello world."):
		"""send sms message"""

		if self.token is None:
			return "Invalid token ", self.token

		if len(num) != 10:
			# this assumes the numbers are in the format of 04xxxxxxxx. Make sure you format accordingly beforehand. 
			return "Invalid Australian Phone number"

		headers_msg = {
			'Authorization': 'Bearer {0}'.format(self.token)
		}

		params_msg = {
			'to': num,
			'body': sms_text,
		}

		try:
			r = requests.post(REQUEST_MSG_URL, data=json.dumps(params_msg), headers=headers_msg)
			return json.loads(r.text)['messageId']
		except RequestException as e:
			print(str(e))
			
	def sms_status(self, messageID):
		"""check sent SMS status"""
		
		if self.token is None:
			return "Invalid token ", self.token
			
		headers_msg = {
			'Authorization': 'Bearer {0}'.format(self.token)
		}
		
		STATUS_URL = REQUEST_MSG_URL + "/" + messageID
		
		try:
			r = requests.get(STATUS_URL, '', headers=headers_msg)
			return json.loads(r.text)
		except RequestException as e:
			print(str(e))
			
	def sms_response(self, messageID):
		"""gets SMS response (i.e. when someone replies to a message from us"""
		
		if self.token is None:
			return "Invalid token ", self.token
			
		headers_msg = {
			'Authorization': 'Bearer {0}'.format(self.token)
		}
		
		RESPONSE_URL = REQUEST_MSG_URL + "/" + messageID + "/response"
		
		try:
			r = requests.get(RESPONSE_URL, '', headers=headers_msg)
			return json.loads(r.text)
		except RequestException as e:
			print(str(e))
			
	def get_quota(self):
		"""
			This uses a somewhat undocumented API, and may be deprecated one day.
			Official word from Telstra is (October 26, 2016):
				'Usually, the SMS quota information can be seen in the Developer Portal under ‘My Apps’, but there’s currently a bug so it’s not visible. Please note that you shouldn’t add this endpoint to your app, as it is not officially supported and can be removed in the future. This is because another implementation of ‘getting quota details’ is in the works.'
		"""
		
		if self.token is None:
			return "Invalid token ", self.token
			
		headers_msg = {
			'Authorization': 'Bearer {0}'.format(self.token)
		}
				
		try:
			r = requests.get(QUOTA_URL, '', headers=headers_msg)
			return json.loads(r.text)
		except RequestException as e:
			print(str(e))
		
		
		










