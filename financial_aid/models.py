from colleges.models import CollegeStatus
from django.db import models
from django_better_admin_arrayfield.models.fields import ArrayField


DEFAULT_AID_CATEGORY_ID = 1
DEFAULT_COLLEGE_STATUS_ID = 1
DEFAULT_DOCUMENT_RESULT_ID = 14

################################################################################
# Relied on by other models
################################################################################
class DocumentResult(models.Model):
    college_status = models.ForeignKey(
        CollegeStatus,
        default=DEFAULT_COLLEGE_STATUS_ID,
        on_delete=models.CASCADE
    )
    document_name = models.CharField(max_length=255, unique=True)
    sent = models.BooleanField(default=False)

    # table analysis
    table_job_id = models.CharField(blank=True, max_length=255)
    table_succeeded = models.BooleanField(blank=True, null=True)
    table_data = models.TextField(blank=True)

    # text analysis
    text_job_id = models.CharField(blank=True, max_length=255)
    text_succeeded = models.BooleanField(blank=True, null=True)
    text_data = ArrayField(
        models.CharField(blank=True, max_length=255),
        blank=True,
        null=True
    )

    # parse data
    automated_review_succeeded = models.BooleanField(blank=True, null=True)
    comparison_missing_num = models.PositiveIntegerField(blank=True, null=True)
    comparison_missing_amounts = ArrayField(
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

################################################################################
# Models
################################################################################
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
    document_result = models.ForeignKey(
        DocumentResult,
        default=DEFAULT_DOCUMENT_RESULT_ID,
        on_delete=models.CASCADE
    )
    aid_category = models.ForeignKey(
        AidCategory,
        default=DEFAULT_AID_CATEGORY_ID,
        on_delete=models.PROTECT
    )
    name = models.CharField(max_length=255)
    amount = models.PositiveIntegerField()
    table_num = models.PositiveSmallIntegerField(blank=True, null=True)
    row_num = models.PositiveSmallIntegerField(blank=True, null=True)
    row_text = ArrayField(
        models.CharField(blank=True, max_length=255),
        blank=True,
        null=True
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'aid data'
        verbose_name_plural = 'aid data'

    def __str__(self):
        return self.name


class DocumentError(models.Model):
    document_result = models.ForeignKey(
        DocumentResult,
        default=DEFAULT_DOCUMENT_RESULT_ID,
        on_delete=models.CASCADE
    )
    type = models.CharField(max_length=255)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'document error'
        verbose_name_plural = 'document errors'

    def __str__(self):
        return str(self.document_result)
