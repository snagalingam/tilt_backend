from twilio.rest import Client
from django.conf import settings

client = Client(
    settings.TWILIO_ACCOUNT, 
    settings.TWILIO_AUTH)

def send_notification_sms(user_number):
    try:
        message = client.messages.create(
            to=user_number, 
            from_=f"+1{settings.TWILIO_NUMBER}",
            body="""
            We finished reviewing your award letter! Check back at www.tiltaccess.com to see your report.
            """)
    except Exception as e:
        print(e)
        raise e 