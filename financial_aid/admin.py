from colleges.models import CollegeStatus
from django.contrib import admin
from django.db import models
from django.forms import Textarea, TextInput
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
from django_better_admin_arrayfield.models.fields import ArrayField
from django_better_admin_arrayfield.forms.widgets import DynamicArrayTextareaWidget
from financial_aid.models import AidCategory, AidData, DocumentError, DocumentResult


################################################
### Inline
################################################
class DocumentError(admin.TabularInline):
    model = DocumentError
    extra = 0
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 5, 'cols': 100})},
    }


################################################
### Admin Panel
################################################
class AidCategoryAdmin(admin.ModelAdmin):
    fieldsets = ((('Information'), {'fields': (
        'name',
        'primary',
        'secondary',
        'tertiary',
        'created',
        'updated',
    )}),)
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size': '50'})},
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
    }
    list_display = ['name', 'primary', 'secondary', 'tertiary',]
    model = AidCategory
    ordering = ('name',)
    readonly_fields = ('created', 'updated',)
    search_fields = ('name', 'primary', 'secondary', 'tertiary',)

    def data_count(self, obj):
        return obj.data_set.count()


class AidDataAdmin(admin.ModelAdmin, DynamicArrayMixin):
    fieldsets = (
        (('Information'), {'fields': (
            'name',
            'amount',
            'college_status',
            'document_result',
            'aid_category',
        )}),
        (('Details'), {'fields': (
            'table_num',
            'row_num',
            'row_text',
            'created',
            'updated',
        )}),
    )
    formfield_overrides = {
        ArrayField: {'widget': DynamicArrayTextareaWidget},
        models.CharField: {'widget': TextInput(attrs={'size': '100'})},
        models.IntegerField: {'widget': TextInput(attrs={'size': '30'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 5, 'cols': 100})},
    }
    list_display = ['college_status', 'name', 'amount', 'aid_category',]
    model = AidData
    ordering = ('name', 'aid_category',)
    readonly_fields = ('created', 'updated',)
    search_fields = ('amount', 'aid_category', 'college_status', 'name')


class DocumentResultAdmin(admin.ModelAdmin, DynamicArrayMixin):
    fieldsets = (
        (('Information'), {'fields': (
            'document_name',
            'college_status',
            'sent',
            'automated_review_succeeded',
            'created',
            'updated',
        )}),
        (('Tables'), {'fields': ('table_job_id', 'table_succeeded', 'table_data',)}),
        (('Text'), {'fields': ('text_job_id', 'text_succeeded', 'text_data')}),
        (('Comparison'), {'fields': ('comparison_missing_num', 'comparison_missing_amounts',)}),
    )
    formfield_overrides = {
        ArrayField: {'widget': DynamicArrayTextareaWidget},
        models.TextField: {'widget': Textarea(attrs={'rows': 8, 'cols': 100})},
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
    }
    inlines = [DocumentError]
    list_display = [
        'document_name',
        'college_status',
        'sent',
        'automated_review_succeeded',
        'created',
    ]
    model = DocumentResult
    ordering = ('college_status', 'document_name',)
    readonly_fields = ('created', 'updated',)
    search_fields = (
        'created',
        'college_status',
        'document_name',
        'sent',
    )


admin.site.register(AidCategory, AidCategoryAdmin)
admin.site.register(AidData, AidDataAdmin)
admin.site.register(DocumentResult, DocumentResultAdmin)
