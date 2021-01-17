from colleges.models import CollegeStatus
from django.db.models.signals import pre_save
from django.dispatch import receiver
from services.sendgrid_api.send_email import send_notification_email
from services.twilio_api.sms_methods import send_notification_sms


@receiver(pre_save, sender=CollegeStatus, dispatch_uid='contact_user')
def contact_user(sender, instance, **kwargs):
    award_status = instance.award_status
    contact_method = instance.user.preferred_contact_method
    user = instance.user

    # send user notification about financial aid letter if award_reviewed=True
    if award_status == "reviewed":

        if contact_method == "text":
            send_notification_sms(user.phone_number)
            award_status = "texted user"

        else:
            send_notification_email(user.email, user.first_name)
            award_status = "emailed user"
