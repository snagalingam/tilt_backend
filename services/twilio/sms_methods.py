from twilio.rest import Client
from django.conf import settings

client = Client(
    settings.TWILIO_ACCOUNT_SID,
    settings.TWILIO_AUTH_TOKEN
)

def send_award_notification_sms(phone_number, college):
    try:
        message = client.messages.create(
            to=f"+1{phone_number}",
            from_=settings.TWILIO_PHONE_NUMBER,
            body=f"""
            We finished reviewing your financial aid award letter for {college}!
            Check back at www.tiltaccess.com to see your report.
            """
        )
    except Exception as e:
        raise e
