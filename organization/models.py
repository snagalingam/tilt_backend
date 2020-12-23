from django.db import models
from django_better_admin_arrayfield.models.fields import ArrayField


class Organization(models.Model):
    name = models.CharField(max_length=255)
    place_id = models.CharField(max_length=255, blank=True)
    business_status = models.CharField(max_length=255, blank=True)
    icon = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=255, blank=True)
    lat = models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)
    lng = models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)
    url = models.TextField(blank=True)
    website = models.TextField(blank=True)
    types = ArrayField(
        models.CharField(max_length=255, blank=True),
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
