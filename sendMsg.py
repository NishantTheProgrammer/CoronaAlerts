def send(to, msg):
    import os
    from twilio.rest import Client
    from twilio.http.http_client import TwilioHttpClient

    proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https': os.environ['https_proxy']}


    client = Client()
    # client = Client(http_client=proxy_client)

    # this is the Twilio sandbox testing number
    from_whatsapp_number='whatsapp:+14155238886'
    # replace this number with your own WhatsApp Messaging number
    to_whatsapp_number=f'whatsapp:{to}'

    client.messages.create(body=msg,
                        from_=from_whatsapp_number,
                        to=to_whatsapp_number)
    print(f'{msg} sent to {to}')