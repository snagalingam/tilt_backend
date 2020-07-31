import os
import json
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *

## Make sure sendgrid and _certifi (SSL) is installed and updated then `source .env` is executed

# -------------- To Verify Email Address
# Template ID: d-274ce0ccdabc445eb7c488c7c98695e6


def send_verification(email, first_name):

    message = Mail(
        from_email='hello@tiltaccess.com',
        to_emails=email,
    )

    token = jwt.encode({'user': email}, os.environ.get('SECRET_KEY'),
                       algorithm='HS256').decode('utf-8')

    url = f"https://www.tiltaccess.com/verify-email/{token}"

    message.template_id = 'd-274ce0ccdabc445eb7c488c7c98695e6'
    message.dynamic_template_data = {
        "first_name": first_name,
        "email": email,
        "verification_url": url
    }

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
    except Exception as e:
        print(e)

# -------------- To Reset Password
# Template ID: d-721a69f0688d484db91503c611d87d1c


def send_forgot_password(email, url, first_name):

    message = Mail(
        from_email='hello@tiltaccess.com',
        to_emails=email,
    )

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
        print(response.headers)
    except Exception as e:
        print(e)


# send_verification("dansteryoo@gmail.com",
#                   "https://www.tiltaccess.com", "Danny")
# send_forgot_password("dansteryoo@gmail.com", "https://www.tiltaccess.com", "Danny")
