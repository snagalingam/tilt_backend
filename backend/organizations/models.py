from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.postgres.fields import ArrayField

class Organization(models.Model):
    
    # google api inputted
    place_id = models.CharField(max_length=250, blank=True, null=True)
    business_status = models.CharField(max_length=25, blank=True, null=True)
    icon = models.CharField(max_length=250, blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    phone_number = models.CharField(max_length=25, null=True, blank=True)
    lat = models.CharField(max_length=250, null=True, blank=True)
    lng = models.CharField(max_length=250, null=True, blank=True)
    url = models.CharField(max_length=250, null=True, blank=True)
    website = models.CharField(max_length=250, null=True, blank=True)
    types = ArrayField(
        models.CharField(max_length=250, null=True, blank=True),
        null=True,default=None
    )
    tilt_partnership = models.BooleanField(null=True, blank=True)

    # automatically added
    members = models.ManyToManyField(get_user_model())
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name