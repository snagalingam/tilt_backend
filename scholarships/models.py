from django.conf import settings
from django.db import models
from django_better_admin_arrayfield.models.fields import ArrayField
from django.utils import timezone
from colleges.models import College

class Provider(models.Model):
    organization = models.CharField(max_length=255, null=True, blank=True, unique=True)
    reference = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    zipcode = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    phone_number_ext = models.CharField(max_length=255, null=True, blank=True)

    # automatically added
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.organization)

class Scholarship(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    provider = models.ForeignKey(
        Provider, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    website = models.TextField(null=True, blank=True)
    deadline = models.DateField(null=True, blank=True)
    date_added = models.DateTimeField(default=timezone.now)
    max_amount = models.IntegerField(null=True, blank=True)
    renewable = models.BooleanField(null=True, blank=True)
    number_awards = models.IntegerField(null=True, blank=True)
    education_level = ArrayField(
        models.CharField(max_length=255, null=True, blank=True),
        null=True, blank=True,
    )
    education_requirements = models.TextField(null=True, blank=True)
    area_of_study = ArrayField(
        models.CharField(max_length=255, null=True, blank=True),
        null=True, blank=True,
    )
    area_of_study_description = models.TextField(null=True, blank=True)
    writing_competition = models.BooleanField(null=True, blank=True)
    interest_description = models.CharField(max_length=255, null=True, blank=True)
    college = models.ManyToManyField(College, blank=True)
    association_requirement = ArrayField(
        models.CharField(max_length=255, null=True, blank=True),
        null=True, blank=True,
    )
    location = models.TextField(null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    ethnicity = ArrayField(
        models.CharField(max_length=255, null=True, blank=True),
        null=True, blank=True,
    )
    gender = models.CharField(max_length=255, null=True, blank=True)
    min_gpa = models.FloatField(null=True, blank=True)
    max_gpa = models.FloatField(null=True, blank=True)
    min_act = models.IntegerField(null=True, blank=True)
    min_sat = models.IntegerField(null=True, blank=True)
    disability = models.TextField(null=True, blank=True)
    military = models.TextField(null=True, blank=True)
    citizenship = ArrayField(
        models.CharField(max_length=255, null=True, blank=True),
        null=True, blank=True,
    )
    first_generation = models.BooleanField(null=True, blank=True)
    financial_need = models.BooleanField(null=True, blank=True)

    # automatically added
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

class Status(models.Model):
    user = models.ManyToManyField(
        settings.AUTH_USER_MODEL, 
        related_name='scholarship_status')
    scholarship = models.ForeignKey(
        Scholarship, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, null=True, blank=True)
    
    # automatically added
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Scholarship statuses'

    def __str__(self):
        return str(self.status)