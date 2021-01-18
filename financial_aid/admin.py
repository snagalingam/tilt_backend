from colleges.models import CollegeStatus
from django.contrib import admin
from django.db import models
from django.forms import Textarea, TextInput
from financial_aid.models import AidCategory, AidData, DocumentResult


################################################
### Inline
################################################
class AidDataInline(admin.TabularInline):
    model = AidData
    extra = 0
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '20'})},
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
    inlines = [AidDataInline]
    list_display = ['name', 'primary', 'secondary', 'tertiary',]
    model = AidCategory
    ordering = ('name',)
    readonly_fields = ('created', 'updated',)
    search_fields = ('name', 'primary', 'secondary', 'tertiary',)

    def data_count(self, obj):
        return obj.data_set.count()


class AidDataAdmin(admin.ModelAdmin):
    fieldsets = (
        (('Information'), {'fields': ('name', 'amount', 'college_status', 'aid_category',)}),
        (('Details'), {'fields': (
            'row_text',
            'table',
            'row_index',
            'col_index',
            'created',
            'updated',
        )}),
    )
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
        models.IntegerField: {'widget': TextInput(attrs={'size': '30'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 5, 'cols': 100})},
    }
    list_display = ['college_status', 'name', 'amount', 'aid_category',]
    model = AidData
    ordering = ('name', 'aid_category',)
    readonly_fields = ('created', 'updated',)
    search_fields = ('amount', 'aid_category', 'college_status', 'name')


class DocumentResultAdmin(admin.ModelAdmin):
    fieldsets = (
        (('Information'), {'fields': (
            'document_name',
            'sent',
            'pass_fail',
            'created',
            'updated',
        )}),
        (('Tables'), {'fields': ('table_job_id', 'table_succeeded', 'table_data',)}),
        (('Text'), {'fields': ('text_job_id', 'text_succeeded', 'text_data')}),
        (('Missing'), {'fields': ('number_of_missing', 'missing_amounts',)}),
    )
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
        models.IntegerField: {'widget': TextInput(attrs={'size': '50'})},
    }
    list_display = [
        'document_name',
        'sent',
        'processed',
        'pass_fail',
        'number_of_missing',
        'created',
    ]
    model = DocumentResult
    ordering = ('document_name',)
    readonly_fields = ('created', 'updated',)
    search_fields = (
        'created',
        'document_name',
        'sent',
    )


admin.site.register(AidCategory, AidCategoryAdmin)
admin.site.register(AidData, AidDataAdmin)
admin.site.register(DocumentResult, DocumentResultAdmin)
