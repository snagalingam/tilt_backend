from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from colleges.models import College
from services.sendgrid_api.send_email import send_notification_email

class CollegeStatus(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    college = models.ForeignKey(
        College, on_delete=models.CASCADE)

    status = models.CharField(max_length=255, blank=True, null=True)
    net_price = models.IntegerField(blank=True, null=True)
    award_uploaded = models.BooleanField(default=False)
    reviewed = models.BooleanField(default=False)
    user_notified = models.BooleanField(default=False)

    # automatically added
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name_plural = 'college statuses'
    
    def save(self, *args, **kwargs):
        method = self.user.preferred_contact_method

        # send user notification about financial aid letter if reviewed=True
        if self.reviewed is True and method is not None and self.user_notified is not True:
            self.user_notified = True
            
            if method == "email":
                send_notification_email(self.user.email, self.user.first_name)
            if method == "text":
                print('--------------> text user with twilio (not yet integrated')
        
        return super(CollegeStatus, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.pk)