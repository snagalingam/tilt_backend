from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.postgres.fields import ArrayField


class College(models.Model):

    # college scorecard info
    unit_id = models.CharField(max_length=250, blank=True, null=True)
    ope_id = models.CharField(max_length=250, blank=True, null=True)

    # google api inputted
    place_id = models.CharField(max_length=250, blank=True, null=True)
    business_status = models.CharField(max_length=250, blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    phone_number = models.CharField(max_length=25, null=True, blank=True)
    lat = models.IntegerField(null=True, blank=True)
    lng = models.IntegerField(null=True, blank=True)
    url = models.TextField(null=True, blank=True)
    website = models.TextField(null=True, blank=True)
    favicon = models.TextField(null=True, blank=True)
    main_photo = models.TextField(null=True, blank=True)
    photos = ArrayField(
        models.TextField(null=True, blank=True),
        null=True, default=None
    )
    types = ArrayField(
        models.CharField(max_length=250, null=True, blank=True),
        null=True, default=None
    )

    # automatically added
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name
