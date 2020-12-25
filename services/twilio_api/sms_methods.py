from twilio.rest import Client
from django.conf import settings

client = Client(
    settings.TWILIO_ACCOUNT, 
    settings.TWILIO_AUTH)

def send_notification_sms(user_number):
    try:
        message = client.messages.create(
            to=f"+1{user_number}", 
            from_=settings.TWILIO_NUMBER,
            body="""
            We finished reviewing your award letter! Check back at www.tiltaccess.com to see your report.
            """)
        print(message)
    except Exception as e:
        print(e)
        raise e 