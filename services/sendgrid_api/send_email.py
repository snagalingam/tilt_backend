import os
import jwt
import json
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import datetime

# Make sure sendgrid and _certifi (SSL) is installed and updated then `source .env` is executed

ENVIRONMENT = os.environ.get('ENVIRONMENT', default='production')
if ENVIRONMENT == 'development':
    domain = "http://localhost:3000"
elif ENVIRONMENT == 'production':
    domain = os.environ.get('SENDGRID_DOMAIN')

from_email = os.environ.get('FROM_EMAIL')
sender_name = os.environ.get('SENDER_NAME')

def send_email(message):
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.headers)
    except Exception as e:
        print(e)

# -------------- To Verify Email Address
# Template ID: d-274ce0ccdabc445eb7c488c7c98695e6

def send_verification(email, first_name):
    message = Mail(from_email=(from_email, sender_name),
                   to_emails=email)

    token = jwt.encode({'email': email,
                        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=5)},
                       os.environ.get('SECRET_KEY'),
                       algorithm='HS256',
                       headers={'domain': domain}).decode('utf-8')
    url = f"{domain}/activate/{token}"

    message.template_id = 'd-274ce0ccdabc445eb7c488c7c98695e6'
    message.dynamic_template_data = {
        "first_name": first_name,
        "email": email,
        "verification_url": url
    }

    print(message)
    return send_email(message)

# -------------- To Reset Password
# Template ID: d-721a69f0688d484db91503c611d87d1c

def send_reset_password(email, first_name):
    message = Mail(from_email=(from_email, sender_name),
                   to_emails=email)

    token = jwt.encode({'email': email,
                        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=900)},
                       os.environ.get('SECRET_KEY'),
                       algorithm='HS256',
                       headers={'domain': domain}).decode('utf-8')

    url = f"{domain}/forgot-password/{token}"

    message.template_id = 'd-721a69f0688d484db91503c611d87d1c'
    message.dynamic_template_data = {
        "first_name": first_name,
        "email": email,
        "forgot_password_url": url
    }

    print(message)
    return send_email(message)

# -------------- To Send Password Changed Notification
# Template ID: d-44fdc9534a574732a7fca8b07238db04

def send_password_changed(email, first_name):
    message = Mail(from_email=(from_email, sender_name),
                   to_emails=email)

    message.template_id = 'd-44fdc9534a574732a7fca8b07238db04'
    message.dynamic_template_data = {
        "first_name": first_name,
        "email": email
    }

    print(message)
    return send_email(message)

# -------------- To Send Email Changed Notification
# Template ID: d-4d2c08403ebc4a8cbd582233aaff3da6

def send_email_changed(old_email, new_email, first_name):
    message = Mail(from_email=(from_email, sender_name),
                   to_emails=old_email)

    message.template_id = 'd-4d2c08403ebc4a8cbd582233aaff3da6'
    message.dynamic_template_data = {
        "first_name": first_name,
        "old_email": old_email,
        "new_email": new_email
    }

    print(message)
    return send_email(message)


# -------------- To Send Email Report Of Finanical Aid Processing
# Template ID: d-bf7d5f2ce9244a07bcfde29d24531133

def send_report_email(college_status_id, collection):
    message = Mail(from_email=(from_email, sender_name),
                   to_emails=from_email)

    message.template_id = 'd-bf7d5f2ce9244a07bcfde29d24531133'
    message.dynamic_template_data = {
        "college_status_id": college_status_id,
        "collection": collection
    }

    print(message)
    return send_email(message)


# -------------- To Contact User About Aid Letter
# Template ID: 

def send_notification_email(email, first_name):
    message = Mail(from_email=(from_email, sender_name),
                   to_emails=email)

    message.template_id = ''
    message.dynamic_template_data = {
        "first_name": first_name,
        "email": email,
    }

    print(message)
    return send_email(message)