from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from colleges.models import Status

class Budget(models.Model):
    college_status = models.ForeignKey(
        Status, on_delete=models.CASCADE)

    work_study = models.IntegerField(blank=True, null=True)
    job = models.IntegerField(blank=True, null=True)
    savings = models.IntegerField(blank=True, null=True)
    family = models.IntegerField(blank=True, null=True)
    other_scholarships = models.IntegerField(blank=True, null=True)
    loan_subsideized = models.IntegerField(blank=True, null=True)
    loan_unsubsideized = models.IntegerField(blank=True, null=True)
    loan_plus = models.IntegerField(blank=True, null=True)
    loan_private = models.IntegerField(blank=True, null=True)
    loan_school = models.IntegerField(blank=True, null=True)

    # automatically added
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.pk)
