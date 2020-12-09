from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django_better_admin_arrayfield.models.fields import ArrayField
from django.utils import timezone
from college_status.models import CollegeStatus

class DocumentResult(models.Model):
    # Name of document (s3 file name)
    name = models.CharField(max_length=255, null=True, blank=True, unique=True)
    words_id = models.CharField(max_length=255, null=True, blank=True)
    tables_id = models.CharField(max_length=255, null=True, blank=True)
    sent = models.BooleanField(default=False)
    processed = models.BooleanField(default=False)
    pass_fail = models.CharField(max_length=255, null=True, blank=True)
    number_of_missing = models.IntegerField(blank=True, null=True)
    missing_amounts = ArrayField(
        models.CharField(max_length=255, null=True, blank=True),
        null=True, blank=True,
    )

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
    bucket = models.CharField(max_length=255, null=True, blank=True, unique=True)
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
    missing = models.TextField(null=True, blank=True)

    # automatically added
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.bucket)

class AidCategory(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    # cost, aid, net_price
    main_category = models.CharField(max_length=255, null=True, blank=True)

    # direct, indirect, unknown, grant, work_study, loan, scholarship
    sub_category = models.CharField(max_length=255, null=True, blank=True)

    # total, federal, state, other
    sub_sub_category = models.CharField(max_length=255, null=True, blank=True)
    year = models.IntegerField(blank=True, null=True)

    # automatically added
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name_plural = 'aid categories'

    def __str__(self):
        return str(self.name)

class AidData(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    amount = models.IntegerField(blank=True, null=True)
    table_number = models.IntegerField(blank=True, null=True)
    row_index = models.IntegerField(blank=True, null=True)
    col_index = models.IntegerField(blank=True, null=True)
    row_data = ArrayField(
        models.TextField(null=True, blank=True),
        null=True, blank=True, default=None
    )

    college_status = models.ForeignKey(
        CollegeStatus, on_delete=models.CASCADE)
    aid_category =models.ForeignKey(
        AidCategory, on_delete=models.CASCADE)

    # automatically added
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.name)