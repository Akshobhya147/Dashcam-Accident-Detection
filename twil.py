import os
from twilio.rest import Client



def call(mynum="0000000000",twinum="0000000000"):
	try:
		api_sid="Twilio API SID"
		api_key="Twilio API Key"
		client=Client(api_sid,api_key)
		call=client.calls.create(
			to=mynum,
			from_=twinum,
			)
		print(call.sid)
		print("Successfully called!")
	
	except RuntimeError:
		raise e
		
	

