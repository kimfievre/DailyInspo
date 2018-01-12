#(201) 380-7407
from twilio.rest import Client
import authToken

# Your Account SID from twilio.com/console
account_sid = "AC3a708cd623b9a48d8fa8fef632309eef"
# Your Auth Token from twilio.com/console
auth_token  = authToken.token

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+13474953340", 
    from_="+12013807407",
    body="Hello from Python!")

print(message.sid)