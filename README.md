# telstra-sms-sdk

 A Python SDK to allow you to send and receive SMS using Telstra API
 
`Current version:` 0.0.8
`Support Python version`: >=python 2.6 

If you have any questions or issue, please create an issue or pull request.
 
### Prerequisites

Before you are using this package, please register an App at https://dev.telstra.com/. The service is normally activated within a fews days, so be patient.

----
### To Install

__Method 1: Use `pip`__
```bash
pip install telstra-sms-sdk
```

Highly recommend you to use [virtualenv](https://virtualenv.pypa.io/en/stable/) to create your (`any`) python project.

__Method 2: Manually Install__

https://pypi.python.org/pypi/telstra-sms-sdk

----
### To Use and Example
```python
from telstra_sms_sdk.sms import TelstraSMS


# You can find your CLIENT_ID and CLIENT_SECRET at https://dev.telstra.com/ by selecting My Apps -> APPNAME -> Keys
# CLIENT_ID = Consumer Key
# CLIENT_SECRET = Consumer Secret

ts = TelstraSMS(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

# send a SMS
messageID = ts.send_sms("0400000000", sms_text="Hi this is unit test")

# check it's status, sample response:
# {'to': '61400000000', 'receivedTimestamp': '2017-03-08T00:15:55+11:00', 'sentTimestamp': '2017-03-08T00:15:54+11:00', 'status': 'DELIVRD'} 

status = ts.sms_status(messageID)

# get any replies, sample responses:
# [{'from': '61400000000', 'acknowledgedTimestamp': '2017-03-08T00:03:00+11:00', 'content': 'G'Day cobber'}, {'from': '61400000000', 'acknowledgedTimestamp': '2017-03-08T00:04:00+11:00', 'content': "Stone the crows!}]

responses = ts.sms_response(messageID)

# check your usage quota (useful on the free plan), sample output:
# {'used': '13', 'available': '987', 'expiry': '2017-03-30T11:00:00+11:00'}
quota = ts.get_quota()


```

----
### License
MIT 

----
### Contact
- Email: <github@ryanhunt.net>
- Credits to <arkilis@gmail.com> for the original version. 

