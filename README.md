# telstra-sms-sdk

 A fully tested Python SDK allow you to send sms in a more easy way! 

`Current version:` 0.0.7
`Support Python version`: >=python 2.6 

If you have any questions or issue, please create an issue or pull request.



 
### Prerequisite 

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


# You can find your CLIENT_ID and CLIENT_SERVER at https://dev.telstra.com/ by selecting My Apps -> APPNAME -> Keys
# CLIENT_ID = Consumer Key
# CLIENT_SERVER = Consumer Secret

ts = TelstraSMS(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
ts.send_sms("0400000000", sms_text="Hi this is unit test")
```

----
### License
MIT 

----
### Contact
- Email：<arkilis@gmail.com>
- Email: <github@ryanhunt.net>

