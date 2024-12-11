from twilio.rest import Client

def message(_from="0000000000",_to="0000000000",_body="sup"):
	try:
		account_sid = 'Twilio API SID'
		auth_token = 'Twilio API Key'
		client = Client(account_sid, auth_token)
		message = client.messages.create(
		  from_=_from,
		  body=_body,
		  to=_to
		)
		print(message.sid)
		print("Successfully sent!")
	
	except RuntimeError:
		raise error
