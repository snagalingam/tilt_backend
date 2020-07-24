import os
import json
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *

## Make sure sendgrid and _certifi (SSL) is installed and updated then `source .env` is executed


## -------------- Single Email Case 

# from_email = Email("dansteryoo@gmail.com")
# to_email = To("dansteryoo@gmail.com")
# subject = "Sending with SendGrid is Fun"
# content = Content("text/plain", "and easy to do anywhere, even with Python")
# mail = Mail(from_email, to_email, subject, content)

# print("TEST", os.environ.get('PATH'))

# try:
#     sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
#     response = sg.send(mail)
#     print(response.status_code)
#     print(response.body)
#     print(response.headers)
# except Exception as e:
#     print(e)


## -------------- Dynamic Template Case

message = Mail(
    from_email='dansteryoo@gmail.com',
    to_emails='dansteryoo@gmail.com',
)

message.template_id = 'd-23de07b37b2c429480a92926287e2055'

try:
    sendgrid_client = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sendgrid_client.send(message)
except Exception as e:
    print(e)
