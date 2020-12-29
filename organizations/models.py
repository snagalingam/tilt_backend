from django.db import models
from django_better_admin_arrayfield.models.fields import ArrayField


DEFAULT_CHAR_TEXT = ""


class Organization(models.Model):
    # main information
    name = models.CharField(max_length=255)
    place_id = models.CharField(blank=True, max_length=255)
    partner = models.BooleanField(default=False)

    # additional fields
    address = models.CharField(blank=True, max_length=255)
    business_status = models.CharField(blank=True, max_length=255)
    icon = models.CharField(blank=True, max_length=255)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    phone_number = models.CharField(blank=True, max_length=255)
    types = ArrayField(
        models.CharField(blank=True, max_length=255),
        blank=True,
        null=True
    )
    url = models.TextField(blank=True)
    website = models.TextField(blank=True)

    # automatically added
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'organization'
        verbose_name_plural = 'organizations'

    def __str__(self):
        return self.name
