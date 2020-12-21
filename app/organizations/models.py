from django.db import models
from django_better_admin_arrayfield.models.fields import ArrayField


class Organization(models.Model):

    # google api inputted
    place_id = models.CharField(max_length=255, blank=True, null=True)
    business_status = models.CharField(max_length=255, blank=True, null=True)
    icon = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)
    url = models.TextField(null=True, blank=True)
    website = models.TextField(null=True, blank=True)
    types = ArrayField(
        models.CharField(max_length=255, null=True, blank=True),
        null=True, blank=True, default=None
    )
    tilt_partnership = models.BooleanField(default=False)

    # automatically added
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
