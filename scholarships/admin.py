from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Provider, Scholarship, ScholarshipStatus

from django.forms import TextInput, Textarea
from django.db import models
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

class ProviderAdmin(admin.ModelAdmin, DynamicArrayMixin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
    }
    list_display = ['organization', 'reference', 'email', 'state', ]
    fieldsets = (
        (None, {'fields': ('organization', 'reference', 'email', )}),
        (_('Details'), {
            'fields': ('address', 'city', 'state', 'zipcode', 'phone_number', 'phone_number_ext', )
        }),
    )

    search_fields = ('organization', 'reference', 'email', 'state',)
    ordering = ('organization', 'reference',)
    model = Provider

class ScholarshipAdmin(admin.ModelAdmin, DynamicArrayMixin):
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size': '50'})},
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 3, 'cols': 100})},
    }
    list_display = ['name', 'provider', 'deadline', 'max_amount',]
    filter_horizontal = ('college',) 

    fieldsets = (
        (None, {'fields': ('provider', )}),
        (_('College'), {
            'fields': ('college',),
        }),
        (_('Information'), {
            'fields': ('name', 'description', 'max_amount', 'website', 'number_awards', 'renewable',)
        }),
        (_('Dates'), {
            'fields': ('deadline', 'date_added',)
        }),
        (_('Requirements'), {
            'fields': ('interest_description', 'education_level', 'education_requirements', 'area_of_study', 'area_of_study_description', 'association_requirement', 'citizenship',)
        }),
        (_('Other Requirements'), {
            'fields': ('writing_competition', 'location', 'state', 'disability', 'military', 'ethnicity', 'gender', 'min_gpa', 'max_gpa', 'min_act', 'min_sat', 'first_generation', 'financial_need',)
        }),
    )

    search_fields = ('name', 'provider', 'deadline', 'max_amount',)
    ordering = ('name', 'provider',)
    model = Scholarship

class ScholarshipStatusAdmin(admin.ModelAdmin, DynamicArrayMixin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
    }
    list_display = ['status',]
    filter_horizontal = ('user', 'scholarship',) 

    fieldsets = (
        (None, {'fields': ('user', 'scholarship', 'status', )}),
    )

    search_fields = ('user', 'scholarship', 'status',)
    ordering = ('user', 'scholarship',)
    model = ScholarshipStatus

admin.site.register(Provider, ProviderAdmin)
admin.site.register(Scholarship, ScholarshipAdmin)
admin.site.register(ScholarshipStatus, ScholarshipStatusAdmin)
