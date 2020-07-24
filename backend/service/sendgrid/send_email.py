# authentication/send_email.py
import jwt
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.template.loader import render_to_string
from django import template

from django.conf import settings
settings.configure()

def send_confirmation_email(email):

    token = jwt.encode({'user': email}, os.environ.get('SECRET_KEY'),
                       algorithm='HS256').decode('utf-8')
    context = {
        'small_text_detail': 'Thank you for '
                             'creating an account. '
                             'Please verify your email '
                             'address to set up your account.',
        'email': email,
        'domain': os.environ.get('DOMAIN'),
        'token': token,
    }

    msg_html = render_to_string('email_confirmation.html', context)

    message=Mail(
        # the email that sends the confirmation email
        from_email='hello@tiltaccess.com',
        to_emails=[email],  # list of email receivers
        subject='Account activation',  # subject of your email
        html_content=msg_html
    )

    try:
        sendgrid_client = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sendgrid_client.send(message)
    except Exception as e:
        return str(e)


send_confirmation_email('dansteryoo@gmail.com')
