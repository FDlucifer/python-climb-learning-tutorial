# pip install twilio

from twilio.rest import Client

client = Client("ACa1353df1985066ea097346d4e89f44ea", "")
message = client.message.create(body="ye mai kya kar rha", from_="whatsapp:+14155238886", to="whatsapp:+14155238817")

