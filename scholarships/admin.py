from scholarships.models import Provider, Scholarship, ScholarshipStatus
from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from django.utils.translation import gettext_lazy as _
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin


class ProviderAdmin(admin.ModelAdmin, DynamicArrayMixin):
    fieldsets = (
        (None, {'fields': ('organization', 'addressee', 'email', )}),
        (('Details'), {'fields': ('address', 'city', 'state', 'zipcode',
            'phone_number', 'phone_number_ext',)}),
    )
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
    }
    list_display = ['organization', 'addressee', 'email', 'state', ]
    model = Provider
    ordering = ('organization', 'addressee',)
    search_fields = ('organization', 'addressee', 'email', 'state',)


class ScholarshipAdmin(admin.ModelAdmin, DynamicArrayMixin):
    fieldsets = (
        (None, {'fields': ('provider', )}),
        (('College'), {'fields': ('college',),}),
        (('Information'), {'fields': (
            'name',
            'description',
            'max_amount',
            'website',
            'number_awards',
            'renewable',
        )}),
        (('Dates'), {'fields': ('deadline', 'date_added',)}),
        (('Requirements'), {'fields': (
            'interest_description',
            'education_level',
            'education_requirements',
            'area_of_study',
            'area_of_study_description',
            'association_requirement',
            'citizenship',
        )}),
        (('Other Requirements'), {'fields': (
            'writing_competition',
            'location',
            'state',
            'disability',
            'military',
            'ethnicity',
            'gender',
            'min_gpa',
            'max_gpa',
            'min_act',
            'min_sat',
            'first_generation',
            'financial_need',
        )}),
    )
    filter_horizontal = ('college',)
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size': '50'})},
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 3, 'cols': 100})},
    }
    list_display = ['name', 'provider', 'deadline', 'max_amount',]
    model = Scholarship
    ordering = ('name', 'provider',)
    search_fields = ('name', 'provider', 'deadline', 'max_amount',)


class ScholarshipStatusAdmin(admin.ModelAdmin, DynamicArrayMixin):
    fieldsets = ((None, {'fields': ('user', 'scholarship', 'status', )}),)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
    }
    list_display = ['status', 'scholarship', 'user']
    model = ScholarshipStatus
    ordering = ('user', 'scholarship',)
    search_fields = ('user', 'scholarship', 'status',)


admin.site.register(Provider, ProviderAdmin)
admin.site.register(Scholarship, ScholarshipAdmin)
admin.site.register(ScholarshipStatus, ScholarshipStatusAdmin)
