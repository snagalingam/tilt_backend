from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django_better_admin_arrayfield.models.fields import ArrayField
from django.utils import timezone

class DocumentResult(models.Model):
    # Name of document (s3 file name)
    name = models.CharField(max_length=255, null=True, blank=True, unique=True)
    words_id = models.CharField(max_length=255, null=True, blank=True)
    tables_id = models.CharField(max_length=255, null=True, blank=True)
    sent = models.BooleanField(default=False)
    processed = models.BooleanField(default=False)
    pass_fail = models.CharField(max_length=255, null=True, blank=True)
    expired = models.BooleanField(default=False)
    start_date = models.DateTimeField(default=timezone.now)

    # automatically added
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.name)

class DocumentData(models.Model):
    # Name of document (s3 file name)
    name = models.CharField(max_length=255, null=True, blank=True, unique=True)
    words = ArrayField(
        models.CharField(max_length=255, null=True, blank=True),
        null=True, blank=True,
    )
    tables = models.TextField(null=True, blank=True)

    # automatically added
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.name)
        
class BucketCheck(models.Model):
    bucket = models.CharField(max_length=255, null=True, blank=True)
    job_dict = models.TextField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    
    # automatically added
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.bucket)

class BucketResult(models.Model):
    bucket = models.CharField(max_length=255, null=True, blank=True)
    total_documents = models.IntegerField(blank=True, null=True)
    passed_count = models.IntegerField(blank=True, null=True)
    passed_list = ArrayField(
        models.CharField(max_length=255, null=True, blank=True),
        null=True, blank=True,
    )
    failed_count = models.IntegerField(blank=True, null=True)
    failed_list = ArrayField(
        models.CharField(max_length=255, null=True, blank=True),
        null=True, blank=True,
    )

    # automatically added
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.bucket)