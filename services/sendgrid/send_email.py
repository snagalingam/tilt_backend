import os
import jwt
import datetime

from django.conf import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


# Make sure sendgrid and _certifi (SSL) is installed

################################################################################
# Standard send email function
################################################################################
def send_email(message):
    try:
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(message)
    except Exception as e:
        return e


################################################################################
# Add subscriber
################################################################################
def add_subscriber(email):
    try:
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.client.asm.groups._(23297).suppressions._(email).delete()
        response2 = sg.client.marketing.contacts.put(
            request_body=dict(
                list_ids=["4dabef7f-34ee-4c60-a4c8-b4525c8115c5"],
                contacts=[{'email': email}]
            )
        )
    except Exception as e:
        return e


################################################################################
# Verify newsletter subscription
################################################################################
def send_subscription_verification(email):
    message = Mail(
        from_email=(settings.FROM_EMAIL, settings.SENDER_NAME),
        to_emails=email
    )
    url = f"{settings.SENDGRID_DOMAIN}/blog/confirmation?email={email}"
    message.template_id = 'd-829a6f7141724253bc15a8b89289faa4'
    message.dynamic_template_data = {
        "email": email,
        "verification_url": url
    }

    return send_email(message)


################################################################################
# Verify user email address
################################################################################
def send_verification(email, first_name):
    message = Mail(
        from_email=(settings.FROM_EMAIL, settings.SENDER_NAME),
        to_emails=email
    )
    token = jwt.encode(
        {
            'email': email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=5)
        },
        settings.SECRET_KEY,
        algorithm='HS256',
        headers={'domain': settings.SENDGRID_DOMAIN}
    )
    url = f"{settings.SENDGRID_DOMAIN}/activate/{token}"
    message.template_id = 'd-274ce0ccdabc445eb7c488c7c98695e6'
    message.dynamic_template_data = {
        "first_name": first_name,
        "email": email,
        "verification_url": url
    }

    return send_email(message)


################################################################################
# Reset password
################################################################################
def send_reset_password(email, first_name):
    message = Mail(
        from_email=(settings.FROM_EMAIL, settings.SENDER_NAME),
        to_emails=email
    )
    token = jwt.encode(
        {
            'email': email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=900)
        },
        settings.SECRET_KEY,
        algorithm='HS256',
        headers={'domain': settings.SENDGRID_DOMAIN}
    )
    url = f"{settings.SENDGRID_DOMAIN}/forgot-password/{token}"
    message.template_id = 'd-721a69f0688d484db91503c611d87d1c'
    message.dynamic_template_data = {
        "first_name": first_name,
        "email": email,
        "forgot_password_url": url
    }

    return send_email(message)


################################################################################
# Send password change notification
################################################################################
def send_password_changed(email, name):
    message = Mail(
        from_email=(settings.FROM_EMAIL, settings.SENDER_NAME),
        to_emails=email
    )
    message.template_id = 'd-44fdc9534a574732a7fca8b07238db04'
    message.dynamic_template_data = {
        "name": name,
        "email": email
    }

    return send_email(message)


################################################################################
# Send email change notification
################################################################################
def send_email_changed(old_email, new_email, name):
    message = Mail(
        from_email=(settings.FROM_EMAIL, settings.SENDER_NAME),
        to_emails=old_email
    )
    message.template_id = 'd-4d2c08403ebc4a8cbd582233aaff3da6'
    message.dynamic_template_data = {
        "name": name,
        "new_email": new_email
    }

    return send_email(message)


################################################################################
# Send team notification a financial aid letter has been uploaded
################################################################################
def send_report_email(college_name, college_status_id, documents, user_email):
    message = Mail(
        from_email=(settings.FROM_EMAIL, settings.SENDER_NAME),
        to_emails=settings.FROM_EMAIL
    )
    message.template_id = 'd-bf7d5f2ce9244a07bcfde29d24531133'
    message.dynamic_template_data = {
        "documents": documents,
        "college_name": college_name,
        "college_status_id": college_status_id,
        "user_email": user_email
    }

    return send_email(message)


################################################################################
# Notify user that their aid letter has been processed
################################################################################
def send_notification_email(email, first_name):
    message = Mail(
        from_email=(settings.FROM_EMAIL, settings.SENDER_NAME),
        to_emails=email
    )
    message.template_id = ''
    message.dynamic_template_data = {
        "first_name": first_name,
        "email": email,
    }

    return send_email(message)
