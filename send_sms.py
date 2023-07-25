from twilio.rest import Client 

account_sid = 'ACCOUNT SID HERE' 
auth_token = 'AUTH TOKEN HERE' 
client = Client(account_sid, auth_token) 

message = client.messages.create(  
    messaging_service_sid = 'MESSAGE SERVICE SID HERE',
    body = 'WHATEVER YOU WANT TO SAY HERE',
    to = 'PHONE NUMBER YOU WOULD LIKE TO SEND TO HERE'
    )

print(message.sid)
