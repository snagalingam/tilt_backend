from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import DocumentResult, DocumentData, BucketResult, BucketCheck

from django.forms import TextInput, Textarea
from django.db import models
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

class DocumentResultAdmin(admin.ModelAdmin, DynamicArrayMixin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '75'})},
    }
    list_display = ['name', 'pass_fail', 'expired', 'start_date']
    fieldsets = (
        (None, {'fields': ('pass_fail',)}),
        (_('Results'), {
            'fields': ('sent', 'processed', 'expired')
        }),
        (_('Details'), {'fields': ('name', 'words_id', 'tables_id')}),
        (_('Dates'), {
            'fields': ('start_date',)
        }),
    )

    search_fields = ('name', 'pass_fail', 'expired', 'start_date',)
    ordering = ('name',)
    model = DocumentResult

admin.site.register(DocumentResult, DocumentResultAdmin)

class DocumentDataAdmin(admin.ModelAdmin, DynamicArrayMixin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '75'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 10, 'cols': 100})},
    }
    list_display = ['name',]
    fieldsets = (
        (_('Tables'), {'fields': ('tables',)}),
        (_('Words'), {'fields': ('words',)}),
    )

    search_fields = ('name',)
    ordering = ('name',)
    model = DocumentData

admin.site.register(DocumentData, DocumentDataAdmin)

class BucketCheckAdmin(admin.ModelAdmin, DynamicArrayMixin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 50, 'cols': 100})},
    }
    list_display = ['bucket', 'date']
    fieldsets = (
        (_('Result'), {'fields': ('job_dict',)}),
        (_('Date'), {'fields': ('date',)}),

    )

    search_fields = ('bucket', 'date')
    ordering = ('bucket', 'date')
    model = BucketCheck

admin.site.register(BucketCheck, BucketCheckAdmin)

class BucketResultAdmin(admin.ModelAdmin, DynamicArrayMixin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '75'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 10, 'cols': 100})},
    }
    list_display = ['bucket', 'total_documents', 'passed_count', 'failed_count']
    fieldsets = (
        (_('Information'), {'fields': ('bucket', 'total_documents')}),
        (_('Results'), {
            'fields': ('passed_count', 'passed_list', 'failed_count', 'failed_list')
        }),
    )

    search_fields = ('bucket',)
    ordering = ('bucket',)
    model = BucketResult

admin.site.register(BucketResult, BucketResultAdmin)