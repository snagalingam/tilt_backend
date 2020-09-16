from django.db import models
from django.contrib.postgres.fields import ArrayField


class Organization(models.Model):

    # google api inputted
    place_id = models.CharField(max_length=255, blank=True, null=True)
    business_status = models.CharField(max_length=255, blank=True, null=True)
    icon = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    lat = models.CharField(null=True, blank=True)
    lng = models.CharField(null=True, blank=True)
    url = models.TextField(null=True, blank=True)
    website = models.TextField(null=True, blank=True)
    types = ArrayField(
        models.CharField(max_length=255, null=True, blank=True),
        null=True, default=None
    )
    tilt_partnership = models.BooleanField(null=True, blank=True, default=False)

    # automatically added
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
