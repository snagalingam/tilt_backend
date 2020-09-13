from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models


class Scholarship(models.Model):

    # user inputted
    name = models.CharField(max_length=255, unique_for_date='deadline')
    organization = models.CharField(max_length=255, blank=True, null=True)
    url = models.URLField(max_length=1000)
    due_date = models.DateField()
    max_amount = models.IntegerField(null=True, blank=True)
    renewable = models.BooleanField(null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    area_of_study = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    ethnicity = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=255, null=True, blank=True)
    gpa = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    us_citizen = models.BooleanField()
    daca_status = models.BooleanField()
    financial_need = models.BooleanField()
    hbcu = models.BooleanField()

    # automatically added
    author = models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
