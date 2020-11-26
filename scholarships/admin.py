from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Scholarship, Organization

from django.forms import TextInput, Textarea
from django.db import models
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

class ScholarshipAdmin(admin.ModelAdmin, DynamicArrayMixin):
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size': '50'})},
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 3, 'cols': 100})},
    }
    list_display = ['name', 'organization', 'deadline', 'max_amount',]
    fieldsets = (
        (_('Information'), {
            'fields': ('name', 'organization', 'description', 'max_amount', 'website', 'number_awards', 'renewable',)
        }),
        (_('Dates'), {
            'fields': ('deadline', 'date_added',)
        }),
        (_('Requirements'), {
            'fields': ('education_level', 'education_requirements', 'area_of_study', 'area_of_study_description', 'association_requirement', 'citizenship',)
        }),
        (_('Other Requirements'), {
            'fields': ('writing_competition', 'location', 'state', 'disability', 'military', 'ethnicity', 'gender', 'min_gpa', 'max_gpa', 'min_act', 'min_sat', 'first_generation', 'financial_need',)
        }),
    )

    search_fields = ('name', 'organization', 'deadline', 'max_amount',)
    ordering = ('name', 'organization',)
    model = Scholarship

class OrganizationAdmin(admin.ModelAdmin, DynamicArrayMixin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
    }
    list_display = ['contact_name', 'email', 'state', ]
    fieldsets = (
        (None, {
            'fields': ('contact_name', 'email', )
        }),
        (_('Details'), {
            'fields': ('address', 'city', 'state', 'zipcode', 'phone_number', 'phone_number_ext', )
        }),
    )

    search_fields = ('contact_name', 'email', 'state',)
    ordering = ('contact_name',)
    model = Organization

admin.site.register(Scholarship, ScholarshipAdmin)
admin.site.register(Organization, OrganizationAdmin)
