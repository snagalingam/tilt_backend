import os
import json
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *

## Make sure sendgrid and _certifi (SSL) is installed and updated then `source .env` is executed

# -------------- To Verify Email Address
# Template ID: d-274ce0ccdabc445eb7c488c7c98695e6

def send_verfication(email, first_name): 

    message = {
        'from': {
            'email': 'hello@tiltaccess.com'
        },
        'personalizations': [{
            'to': [{
                'email': email,
            }],
            "dynamic_template_data": {
                "name": first_name,
                "email": email,
            },
        }],
        'template_id': 'd-274ce0ccdabc445eb7c488c7c98695e6'
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
# Template ID: d-04c1814dea9e411cbc17a802206b2d45


def send_forgot_password(email, first_name):

    message = {
        'from': {
            'email': 'hello@tiltaccess.com'
        },
        'personalizations': [{
            'to': [{
                'email': email,
            }],
            "dynamic_template_data": {
                "name": first_name,
                "email": email,
            },
        }],
        'template_id': 'd-04c1814dea9e411cbc17a802206b2d45'
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


send_verfication("dansteryoo@gmail.com", "Danny")
# send_forgot_password("dansteryoo@gmail.com", "Danny")
