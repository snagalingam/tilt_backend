import os
import jwt
import json
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import datetime

# Make sure sendgrid and _certifi (SSL) is installed and updated then `source .env` is executed

# -------------- To Verify Email Address
# Template ID: d-274ce0ccdabc445eb7c488c7c98695e6

ENVIRONMENT = os.environ.get('ENVIRONMENT', default='production')
if ENVIRONMENT == 'development':
    domain = "http://localhost:3000"
elif ENVIRONMENT == 'production':
    domain = 'https://tilt-staging.vercel.app'


def send_verification(email, first_name):

    message = Mail(from_email='hello@tiltaccess.com',
                   to_emails=email)

    token = jwt.encode({'email': email,
                        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=5)},
                       os.environ.get('SECRET_KEY'),
                       algorithm='HS256',
                       headers={'domain': 'www.tilt-staging.vercel.app'}).decode('utf-8')
    url = f"{domain}/activate/{token}"

    message.template_id = 'd-274ce0ccdabc445eb7c488c7c98695e6'
    message.dynamic_template_data = {
        "first_name": first_name,
        "email": email,
        "verification_url": url
    }

    print(message)

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.headers)
    except Exception as e:
        print(e)

# -------------- To Reset Password
# Template ID: d-721a69f0688d484db91503c611d87d1c


def send_reset_password(email, first_name):

    message = Mail(from_email='hello@tiltaccess.com',
                   to_emails=email)

    token = jwt.encode({'email': email,
                        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=900)},
                       os.environ.get('SECRET_KEY'),
                       algorithm='HS256',
                       headers={'domain': 'www.tilt-staging.vercel.app'}).decode('utf-8')

    url = f"{domain}/forgot-password/{token}"

    message.template_id = 'd-721a69f0688d484db91503c611d87d1c'
    message.dynamic_template_data = {
        "first_name": first_name,
        "email": email,
        "forgot_password_url": url
    }

    print(message)

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.headers)
    except Exception as e:
        print(e)
