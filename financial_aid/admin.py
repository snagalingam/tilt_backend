from colleges.models import CollegeStatus
from django.contrib import admin
from django.db import models
from django.forms import Textarea, TextInput
from financial_aid.models import AidCategory, AidData, DocumentData, DocumentResult, AidSummary


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


class AidSummaryAdmin(admin.ModelAdmin):
    fieldsets = (
        (('Information'), {'fields': (
            'college_status',
            'total_cost',
            'total_aid',
            'net_price',
            'created',
            'updated',
    )}),
    )
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size': '50'})},
    }
    list_display = ['college_status', 'total_cost', 'total_aid', 'net_price',]
    model = AidSummary
    ordering = ('college_status',)
    readonly_fields = ('created', 'updated',)
    search_fields = ('college_status', 'total_cost', 'total_aid', 'net_price',)


class DocumentDataAdmin(admin.ModelAdmin):
    fieldsets = (
        (('Information'), {'fields': ('document_name', 'created', 'updated',)}),
        (('Tables'), {'fields': ('tables',)}),
        (('Words'), {'fields': ('words',)}),
    )
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '75'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 10, 'cols': 100})},
    }
    list_display = ['document_name', 'created']
    model = DocumentData
    ordering = ('document_name',)
    readonly_fields = ('created', 'updated',)
    search_fields = ('document_name',)


class DocumentResultAdmin(admin.ModelAdmin):
    fieldsets = (
        (('Information'), {'fields': (
            'document_name',
            'words_id',
            'tables_id',
            'sent',
            'processed',
            'pass_fail',
            'created',
            'updated',
        )}),
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
        'document_name',
        'sent', 'processed',
        'pass_fail',
        'number_of_missing',
        'created',
    )


admin.site.register(AidCategory, AidCategoryAdmin)
admin.site.register(AidData, AidDataAdmin)
admin.site.register(AidSummary, AidSummaryAdmin)
admin.site.register(DocumentData, DocumentDataAdmin)
admin.site.register(DocumentResult, DocumentResultAdmin)
