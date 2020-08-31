import os
import json
from sendgrid import SendGridAPIClient

# Make sure sendgrid and _certifi (SSL) is installed and updated then `source .env` is executed

# -------------- To add subscriber to list
# List ID: 4dabef7f-34ee-4c60-a4c8-b4525c8115c5

def add_subscriber(email):
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.client.marketing.contacts.put(request_body=dict(
        list_ids=["4dabef7f-34ee-4c60-a4c8-b4525c8115c5"], 
        contacts=[{'email': email}]
    ))
        print(response.status_code)
        print(response.headers)
    except Exception as e:
        print(e)
