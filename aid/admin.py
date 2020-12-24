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
    fieldsets = (
        (None, {'fields': ('name',)}),
        (('Information'), {'fields': ('primary', 'secondary', 'tertiary',)}),
    )
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size': '50'})},
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
    }
    inlines = [DataInline]
    list_display = ['name', 'primary', 'secondary', 'tertiary',]
    model = Category
    ordering = ('name',)

    def data_count(self, obj):
        return obj.data_set.count()



class DataAdmin(admin.ModelAdmin, DynamicArrayMixin):
    fieldsets = (
        (None, {'fields': ('name', 'college_status', 'category',)}),
        (('Table Details'), {'fields': ('amount', 'table_number', 'row_index', 'col_index', 'row_data',)}),
    )
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size': '50'})},
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
    }
    list_display = ['college_status', 'name', 'amount', 'category',]
    model = Data
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


admin.site.register(Category, CategoryAdmin)
admin.site.register(Data, DataAdmin)
admin.site.register(DocumentData, DocumentDataAdmin)
admin.site.register(DocumentResult, DocumentResultAdmin)
