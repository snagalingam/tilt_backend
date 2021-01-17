from colleges.models import CollegeStatus
from django.db import models
from django_better_admin_arrayfield.models.fields import ArrayField


DEFAULT_COLLEGE_STATUS_ID = 1
DEFAULT_AID_CATEGORY_ID = 1
DEFAULT_CHAR_TEXT = ""


class AidCategory(models.Model):
    name = models.CharField(max_length=50)
    primary = models.CharField(max_length=50)
    secondary = models.CharField(max_length=50)
    tertiary = models.CharField(max_length=50, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'aid category'
        verbose_name_plural = 'aid categories'

    def __str__(self):
        return self.name


class AidData(models.Model):
    college_status = models.ForeignKey(
        CollegeStatus,
        default=DEFAULT_COLLEGE_STATUS_ID,
        on_delete=models.CASCADE
    )
    aid_category = models.ForeignKey(
        AidCategory,
        default=DEFAULT_AID_CATEGORY_ID,
        on_delete=models.PROTECT
    )
    name = models.CharField(max_length=255)
    amount = models.PositiveIntegerField()
    row_text = models.TextField(blank=True)
    table = models.PositiveSmallIntegerField(blank=True, null=True)
    row_index = models.PositiveSmallIntegerField(blank=True, null=True)
    col_index = models.PositiveSmallIntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'aid data'
        verbose_name_plural = 'aid data'

    def __str__(self):
        return self.name


class DocumentData(models.Model):
    document_name = models.CharField(max_length=255, unique=True)
    words = ArrayField(
        models.CharField(blank=True, max_length=255),
        blank=True,
        null=True
    )
    tables = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'document data'
        verbose_name_plural = 'document data'

    def __str__(self):
        return self.document_name


class DocumentResult(models.Model):
    document_name = models.CharField(max_length=255, unique=True)
    words_id = models.CharField(max_length=255, blank=True)
    tables_id = models.CharField(max_length=255, blank=True)
    sent = models.BooleanField(default=False)
    processed = models.BooleanField(default=False)
    pass_fail = models.CharField(max_length=255, blank=True)
    number_of_missing = models.PositiveIntegerField(blank=True, null=True)
    missing_amounts = ArrayField(
        models.CharField(blank=True, max_length=255),
        blank=True,
        null=True
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'document result'
        verbose_name_plural = 'document results'

    def __str__(self):
        return self.document_name
