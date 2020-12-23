from .models import Category, Data, DocumentData, DocumentResult
from django.contrib import admin
from django.db import models
from django.forms import Textarea, TextInput
from django.utils.translation import gettext_lazy as _
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin


################################################
### Inline
################################################
class DataInline(admin.TabularInline):
    model = Data
    extra = 0
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '20'})},
    }


################################################
### Admin Panel
################################################
class CategoryAdmin(admin.ModelAdmin, DynamicArrayMixin):
    def data_count(self, obj):
        return obj.data_set.count()

    fieldsets = (
        (None, {'fields': ('name',)}),
        (('Information'), {'fields': ('year', 'main_category', 'sub_category', 'sub_sub_category')}),
    )
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size': '50'})},
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
    }
    inlines = [AidDataInline]
    list_display = ['name', 'year', 'main_category', 'sub_category', 'data_count']
    model = Category
    ordering = ('name', 'year')


class DataAdmin(admin.ModelAdmin, DynamicArrayMixin):
    fieldsets = (
        (None, {'fields': ('name', 'college_status', 'aid_category')}),
        (('Table Details'), {'fields': ('amount', 'table_number', 'row_index', 'col_index', 'row_data')}),
    )
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size': '50'})},
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
    }
    list_display = ['college_status', 'name', 'amount', 'aid_category',]
    model = Data
    ordering = ('name', 'amount', 'college_status', 'aid_category',)
    search_fields = ('name', 'amount', 'college_status', 'aid_category',)


class DocumentDataAdmin(admin.ModelAdmin, DynamicArrayMixin):
    fieldsets = (
        (('Tables'), {'fields': ('tables',)}),
        (('Words'), {'fields': ('words',)}),
    )
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '75'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 10, 'cols': 100})},
    }
    list_display = ['name', ]
    model = DocumentData
    ordering = ('name',)
    search_fields = ('name',)


class DocumentResultAdmin(admin.ModelAdmin, DynamicArrayMixin):
    fieldsets = (
        (None, {'fields':('sent', 'processed', 'pass_fail')}),
        (('Details'), {'fields': ('name', 'words_id', 'tables_id')}),
        (('Missing'), {'fields': ('number_of_missing', 'missing_amounts')}),
    )
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size': '50'})},
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
    }
    list_display = ['name', 'sent', 'processed', 'pass_fail', 'number_of_missing', 'created']
    model = DocumentResult
    ordering = ('name', 'sent', 'processed', 'number_of_missing','created',)
    search_fields = ('name', 'pass_fail', 'number_of_missing', 'created',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Data, DataAdmin)
admin.site.register(DocumentData, DocumentDataAdmin)
admin.site.register(DocumentResult, DocumentResultAdmin)
