from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import DocumentResult, DocumentData, Category, Data, Summary

from django.forms import TextInput, Textarea
from django.db import models
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

class DocumentResultAdmin(admin.ModelAdmin, DynamicArrayMixin):
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size': '50'})},
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
    }
    list_display = ['name', 'sent', 'processed', 'pass_fail', 'number_of_missing', 'created']

    fieldsets = (
        (None, {
            'fields':('sent', 'processed', 'pass_fail',)
        }),
        (_('Details'), {
            'fields': ('name', 'words_id', 'tables_id')
        }),
        (_('Missing'), {
            'fields': ('number_of_missing', 'missing_amounts',)
        }),
    )

    search_fields = ('name', 'pass_fail', 'number_of_missing', 'created',)
    ordering = ('name', 'sent', 'processed', 'number_of_missing', 'created',)
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

class DataInline(admin.TabularInline):
    model = Data
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '20'})},
    }
    extra = 0

class CategoryAdmin(admin.ModelAdmin, DynamicArrayMixin):

    def data_count(self, obj):
        return obj.data_set.count()

    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size': '50'})},
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
    }
    list_display = ['name', 'year', 'main_category', 'sub_category', 'data_count']
    fieldsets = (
        (None, {'fields': ('name',)}),
        (_('Information'), {
            'fields': ('year', 'main_category', 'sub_category', 'sub_sub_category')
        }),
    )

    inlines = [DataInline]

    search_fields = ('name', 'main_category', 'sub_category',)
    ordering = ('name', 'year')
    model = Category

class DataAdmin(admin.ModelAdmin, DynamicArrayMixin):
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size': '50'})},
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
    }
    list_display = ['name', 'amount', 'status', 'category',]
    fieldsets = (
        (None, {'fields': ('name', 'status', 'category')}),
        (_('Table Details'), {
            'fields': ('table_number', 'row_index', 'col_index', 'row_data')
        }),
    )

    search_fields = ('name', 'status__pk', 'category__name')
    ordering = ('status', 'name', 'category')
    model = Data

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

admin.site.register(DocumentResult, DocumentResultAdmin)
admin.site.register(DocumentData, DocumentDataAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Data, DataAdmin)
admin.site.register(Summary, SummaryAdmin)