import os
import json
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Make sure sendgrid and _certifi (SSL) is installed and updated then `source .env` is executed

# -------------- To add subscriber to list
# List ID: 4dabef7f-34ee-4c60-a4c8-b4525c8115c5

# -------------- To send email verification to subscribe
# List ID: d-829a6f7141724253bc15a8b89289faa4

ENVIRONMENT = os.environ.get('ENVIRONMENT', default='production')
if ENVIRONMENT == 'development':
    domain = "http://localhost:3000"
elif ENVIRONMENT == 'production':
    domain = os.environ.get('SENDGRID_DOMAIN')

from_email = os.environ.get('FROM_EMAIL')
sender_name = os.environ.get('SENDER_NAME')


def send_subscription_verification(email):

    message = Mail(from_email=(from_email, sender_name),
                   to_emails=email)

    url = f"{domain}/confirmation#{email}"

    message.template_id = 'd-829a6f7141724253bc15a8b89289faa4'
    message.dynamic_template_data = {
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


def add_subscriber(email):
    try:

        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.client.asm.groups._(23297).suppressions._(email).delete()
        response2 = sg.client.marketing.contacts.put(request_body=dict(
            list_ids=["4dabef7f-34ee-4c60-a4c8-b4525c8115c5"],
            contacts=[{'email': email}]

        ))
        print(response.status_code)
        print(response.headers)
        print(response2.status_code)
        print(response2.headers)
    except Exception as e:
        print(e)
