from django.db import models

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.postgres.fields import ArrayField


class MyCollege(models.Model):

    user_id = models.CharField(max_length=255, blank=True, null=True)
    college_id = models.CharField(max_length=255, blank=True, null=True)

    college_status = models.CharField(max_length=255, blank=True, null=True)
    net_price = models.IntegerField(blank=True, null=True)
    popularity_score = models.IntegerField(blank=True, null=True)
    
    # automatically added
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name
