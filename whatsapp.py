from twilio.rest import Client


def send_text(message):

# client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
    client = Client()

    # this is the Twilio sandbox testing number
    from_whatsapp_number='whatsapp:+14155238886'
    # replace this number with your own WhatsApp Messaging number
    to_whatsapp_number='whatsapp:+33684086800'

    client.messages.create(body=message,
                        from_=from_whatsapp_number,
                        to=to_whatsapp_number)




send_text('SALUT')