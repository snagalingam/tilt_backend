from college.models import Status
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django_better_admin_arrayfield.models.fields import ArrayField


DEFAULT_COLLEGE_STATUS = 1
DEFAULT_CATEGORY = 1

class Category(models.Model):
    name = models.CharField(max_length=255)
    primary = models.CharField(max_length=255)
    secondary = models.CharField(max_length=255)
    tertiary = models.CharField(max_length=255, blank=True)

    # automatically added
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Data(models.Model):
    college_status = models.ForeignKey(
        Status,
        default=DEFAULT_COLLEGE_STATUS,
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        default=DEFAULT_CATEGORY,
        on_delete=models.CASCADE
    )
    name = models.TextField()
    amount = models.PositiveIntegerField()
    row_data = ArrayField(
        models.TextField(null=True, blank=True),
        blank=True,
        null=True
    )
    table_number = models.PositiveIntegerField(blank=True, null=True)
    row_index = models.PositiveIntegerField(blank=True, null=True)
    col_index = models.PositiveIntegerField(blank=True, null=True)

    # automatically added
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'data'
        verbose_name_plural = 'data'

    def __str__(self):
        return str(self.name)


class DocumentData(models.Model):
    document_name = models.CharField(max_length=255, unique=True)
    words = ArrayField(
        models.CharField(max_length=255, null=True, blank=True),
        blank=True,
        null=True
    )
    tables = models.TextField(null=True, blank=True)

    # automatically added
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'document data'
        verbose_name_plural = 'document data'

    def __str__(self):
        return self.name


class DocumentResult(models.Model):
    document_name = models.CharField(max_length=255, unique=True)
    words_id = models.CharField(max_length=255, blank=True)
    tables_id = models.CharField(max_length=255, blank=True)
    sent = models.BooleanField(default=False)
    processed = models.BooleanField(default=False)
    pass_fail = models.CharField(max_length=255, blank=True)
    number_of_missing = models.PositiveIntegerField(blank=True, null=True)
    missing_amounts = ArrayField(
        models.CharField(max_length=255, null=True, blank=True),
        blank=True,
        null=True
    )

    # automatically added
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'document result'
        verbose_name_plural = 'document results'

    def __str__(self):
        return self.name
