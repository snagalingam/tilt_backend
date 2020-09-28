from django.db import models

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from colleges.models import College

class CollegeStatus(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    college = models.ForeignKey(
        College, on_delete=models.CASCADE)

    status = models.CharField(max_length=255, blank=True, null=True)
    net_price = models.IntegerField(blank=True, null=True)

    # automatically added
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name_plural = 'college statuses'

    def __str__(self):
        return str(self.college_id)
