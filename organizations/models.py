from django.db import models
from django_better_admin_arrayfield.models.fields import ArrayField


DEFAULT_CHAR_TEXT = ""


class Organization(models.Model):
    name = models.CharField(
        max_length=255,
        default=DEFAULT_CHAR_TEXT
    )
    place_id = models.CharField(
        max_length=255,
        default=DEFAULT_CHAR_TEXT
    )
    business_status = models.CharField(
        max_length=255,
        default=DEFAULT_CHAR_TEXT
    )
    icon = models.CharField(
        max_length=255,
        default=DEFAULT_CHAR_TEXT
    )
    address = models.CharField(
        max_length=255,
        default=DEFAULT_CHAR_TEXT
    )
    phone_number = models.CharField(
        max_length=255,
        default=DEFAULT_CHAR_TEXT
    )
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    url = models.TextField(default=DEFAULT_CHAR_TEXT)
    website = models.TextField(default=DEFAULT_CHAR_TEXT)
    types = ArrayField(
        models.CharField(
        max_length=255,
        default=DEFAULT_CHAR_TEXT
    ),
        null=True, blank=True, default=None
    )
    partner = models.BooleanField(default=False)

    # automatically added
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'organization'
        verbose_name_plural = 'organizations'

    def __str__(self):
        return self.name
