from .models import AidCategory, AidData, DocumentData, DocumentResult
from django.contrib import admin
from django.db import models
from django.forms import Textarea, TextInput
from django.utils.translation import gettext_lazy as _
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin


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
class AidCategoryAdmin(admin.ModelAdmin, DynamicArrayMixin):
    fieldsets = (
        (None, {'fields': ('name',)}),
        (('Information'), {'fields': ('primary', 'secondary', 'tertiary',)}),
    )
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size': '50'})},
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
    }
    inlines = [AidDataInline]
    list_display = ['name', 'primary', 'secondary', 'tertiary',]
    model = AidCategory
    ordering = ('name',)

    def data_count(self, obj):
        return obj.data_set.count()



class AidDataAdmin(admin.ModelAdmin, DynamicArrayMixin):
    fieldsets = (
        (None, {'fields': ('name', 'college_status', 'category',)}),
        (('Table Details'), {'fields': ('amount', 'table_number', 'row_index', 'col_index', 'row_data',)}),
    )
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size': '50'})},
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
    }
    list_display = ['college_status', 'name', 'amount', 'category',]
    model = AidData
    ordering = ('name', 'amount', 'college_status', 'category',)
    search_fields = ('name', 'amount', 'college_status', 'category',)


class DocumentDataAdmin(admin.ModelAdmin, DynamicArrayMixin):
    fieldsets = (
        (('Tables'), {'fields': ('tables',)}),
        (('Words'), {'fields': ('words',)}),
    )
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '75'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 10, 'cols': 100})},
    }
    list_display = ['document_name',]
    model = DocumentData
    ordering = ('document_name',)
    search_fields = ('document_name',)


class DocumentResultAdmin(admin.ModelAdmin, DynamicArrayMixin):
    fieldsets = (
        (None, {'fields':('sent', 'processed', 'pass_fail',)}),
        (('Details'), {'fields': ('document_name', 'words_id', 'tables_id',)}),
        (('Missing'), {'fields': ('number_of_missing', 'missing_amounts',)}),
    )
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size': '50'})},
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
    }
    list_display = ['document_name', 'sent', 'processed', 'pass_fail', 'number_of_missing', 'created',]
    model = DocumentResult
    ordering = ('document_name', 'sent', 'processed', 'number_of_missing', 'created',)
    search_fields = ('document_name', 'pass_fail', 'number_of_missing', 'created',)

class SummaryAdmin(admin.ModelAdmin, DynamicArrayMixin):
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size': '50'})},
    }
    list_display = ['status', 'total_cost', 'total_aid', 'net_price',]
    fieldsets = (
        (None, {'fields': ('status', 'total_cost', 'total_aid', 'net_price',)}),
    )

    search_fields = ('status__pk', 'total_cost', 'total_aid', 'net_price',)
    ordering = ('status__pk',)
    model = Summary
    
admin.site.register(AidCategory, AidCategoryAdmin)
admin.site.register(AidData, AidDataAdmin)
admin.site.register(DocumentData, DocumentDataAdmin)
admin.site.register(DocumentResult, DocumentResultAdmin)
admin.site.register(Summary, SummaryAdmin)