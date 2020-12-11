from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import DocumentResult, DocumentData, BucketResult, BucketCheck, AidCategory, AidData

from django.forms import TextInput, Textarea
from django.db import models
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

class DocumentResultAdmin(admin.ModelAdmin, DynamicArrayMixin):
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size': '50'})},
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
    }
    list_display = ['name', 'processed', 'pass_fail', 'number_of_missing', 'reviewed', 'created']
    list_editable = ['reviewed',]

    fieldsets = (
        (None, {
            'fields':('sent', 'processed', 'pass_fail', 'reviewed')
        }),
        (_('Details'), {
            'fields': ('name', 'words_id', 'tables_id')
        }),
        (_('Missing'), {
            'fields': ('number_of_missing', 'missing_amounts',)
        }),
    )

    search_fields = ('name', 'pass_fail', 'number_of_missing', 'created',)
    ordering = ('name', 'number_of_missing','created',)
    model = DocumentResult

class DocumentDataAdmin(admin.ModelAdmin, DynamicArrayMixin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '75'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 10, 'cols': 100})},
    }
    list_display = ['name', ]
    fieldsets = (
        (_('Tables'), {'fields': ('tables',)}),
        (_('Words'), {'fields': ('words',)}),
    )

    search_fields = ('name',)
    ordering = ('name',)
    model = DocumentData

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

class BucketResultAdmin(admin.ModelAdmin, DynamicArrayMixin):
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size': '50'})},
        models.CharField: {'widget': TextInput(attrs={'size': '75'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 10, 'cols': 100})},
    }
    list_display = ['bucket', 'total_documents', 'passed_count', 'failed_count']
    fieldsets = (
        (_('Information'), {'fields': ('bucket', 'total_documents')}),
        (_('Results'), {
            'fields': ('passed_count', 'passed_list', 'failed_count', 'failed_list')
        }),
        (_('Missing'), {
            'fields': ('missing',)
        }),
    )

    search_fields = ('bucket',)
    ordering = ('bucket',)
    model = BucketResult

class AidDataInline(admin.TabularInline):
    model = AidData
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '20'})},
    }
    extra = 0

class AidCategoryAdmin(admin.ModelAdmin, DynamicArrayMixin):

    def aid_data_count(self, obj):
        return obj.aiddata_set.count()

    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size': '50'})},
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
    }
    list_display = ['name', 'year', 'main_category', 'sub_category', 'aid_data_count']
    fieldsets = (
        (None, {'fields': ('name',)}),
        (_('Information'), {
            'fields': ('year', 'main_category', 'sub_category', 'sub_sub_category')
        }),
    )

    inlines = [AidDataInline]

    search_fields = ('name', 'main_category', 'sub_category',)
    ordering = ('name', 'year')
    model = AidCategory

class AidDataAdmin(admin.ModelAdmin, DynamicArrayMixin):
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size': '50'})},
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
    }
    list_display = ['name', 'amount', 'college_status', 'aid_category',]
    fieldsets = (
        (None, {'fields': ('name', 'college_status', 'aid_category')}),
        (_('Table Details'), {
            'fields': ('table_number', 'row_index', 'col_index', 'row_data')
        }),
    )

    search_fields = ('name', 'college_status__pk', 'aid_category__name')
    ordering = ('college_status', 'name', 'aid_category')
    model = AidData

admin.site.register(DocumentResult, DocumentResultAdmin)
admin.site.register(DocumentData, DocumentDataAdmin)
admin.site.register(BucketCheck, BucketCheckAdmin)
admin.site.register(BucketResult, BucketResultAdmin)
admin.site.register(AidCategory, AidCategoryAdmin)
admin.site.register(AidData, AidDataAdmin)