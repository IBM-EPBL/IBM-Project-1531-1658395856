from twilio.rest import Client 
 
account_sid = 'ACe298c07762917a3dc43b81a2f64bb0ad' 
auth_token = '80158c193c30d15b7ca4c3668f24bfec' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(from_="+12136421417",messaging_service_sid="MG4c7b0e964084e40262698922a5db931c",body="Forest Fire Is Detected , Stay Alert",to="+919884330848") 
 
print(message.sid)