import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}


client = Client(http_client=proxy_client)

# this is the Twilio sandbox testing number
from_whatsapp_number='whatsapp:+14155238886'
# replace this number with your own WhatsApp Messaging number
to_whatsapp_number='whatsapp:+918860009709'

client.messages.create(body='from=>pythoneverywhare, world!',
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)