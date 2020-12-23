from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from colleges.models import College

class CollegeStatus(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    college = models.ForeignKey(
        College, on_delete=models.CASCADE, default=1)

    status = models.CharField(max_length=255, blank=True, null=True)
    net_price = models.IntegerField(blank=True, null=True)
    award_uploaded = models.BooleanField(default=False)
    reviewed = models.BooleanField(default=False)
    user_notified = models.BooleanField(default=False)

    # automatically added
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.pk)
