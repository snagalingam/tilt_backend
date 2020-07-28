from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models


class Organization(models.Model):

    # user inputted
    place_id = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    formatted_address = models.CharField(max_length=250, blank=True, null=True)
    formatted_phone_number = models.CharField(max_length=15, null=True, blank=True)
    geo_location = models.CharField(max_length=250, null=True, blank=True)
    business_status = models.CharField(max_length=250, null=True, blank=True)
    url = models.CharField(max_length=250, null=True, blank=True)
    website = models.CharField(max_length=250, null=True, blank=True)
    partnership = models.BooleanField(null=True, blank=True)

    # automatically added
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
