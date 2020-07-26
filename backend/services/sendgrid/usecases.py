import os
import json
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *

## Make sure sendgrid and _certifi (SSL) is installed and updated then `source .env` is executed

# -------------- To Verify Email Address
# Template ID: d-274ce0ccdabc445eb7c488c7c98695e6

def send_verfication(email, url, first_name): 

    message = Mail(
        from_email='hello@tiltaccess.com',
        to_emails=email,
    )

    message.template_id = 'd-274ce0ccdabc445eb7c488c7c98695e6'
    message.dynamic_template_data = {
        "first_name": first_name,
        "email": email,
        "verification_url": url
    }

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print("MAIL", message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
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
        print("MAIL", message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)


# send_verfication("dansteryoo@gmail.com", "https://www.tiltaccess.com", "Danny")
# send_forgot_password("dansteryoo@gmail.com", "https://www.tiltaccess.com", "Danny")
