from django.contrib import admin
from django.db import models
from django.forms import Textarea, TextInput
from scholarships.models import (
    Association,
    Citizenship,
    Degree,
    Disability,
    EducationCategory,
    EducationDetail,
    EducationScholarship,
    Field,
    Gender,
    Heritage,
    Interest,
    LocationDetail,
    LocationScholarship,
    Military,
    Provider,
    Scholarship,
    ScholarshipStatus,
    State,
)


################################################
### Inlines
################################################
class EducationScholarshipInline(admin.StackedInline):
    extra = 0
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '20'})},
    }
    model = EducationScholarship

class LocationScholarshipInline(admin.StackedInline):
    extra = 0
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '20'})},
    }
    model = LocationScholarship


################################################
### Objects on Admin Panel
################################################
class AssociationAdmin(admin.ModelAdmin):
    fieldsets = ((None, {'fields': ('name', 'created', 'updated')}),)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
    }
    list_display = ['name',]
    model = Association
    ordering = ('name',)
    readonly_fields = ('created', 'updated')
    search_fields = ('name',)


class CitizenshipAdmin(admin.ModelAdmin):
    fieldsets = ((None, {'fields': ('category', 'created', 'updated')}),)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
    }
    list_display = ['category',]
    model = Citizenship
    ordering = ('category',)
    readonly_fields = ('created', 'updated')
    search_fields = ('category',)


class DegreeAdmin(admin.ModelAdmin):
    fieldsets = ((None, {'fields': ('category', 'created', 'updated')}),)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
    }
    list_display = ['category',]
    model = Degree
    ordering = ('category',)
    readonly_fields = ('created', 'updated')
    search_fields = ('category',)


class DisabilityAdmin(admin.ModelAdmin):
    fieldsets = ((None, {'fields': ('category', 'created', 'updated')}),)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
    }
    list_display = ['category',]
    model = Disability
    ordering = ('category',)
    readonly_fields = ('created', 'updated')
    search_fields = ('category',)


class EducationCategoryAdmin(admin.ModelAdmin):
    fieldsets = ((None, {'fields': ('category', 'created', 'updated')}),)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
    }
    list_display = ['category',]
    model = EducationCategory
    ordering = ('category',)
    readonly_fields = ('created', 'updated')
    search_fields = ('category',)


class EducationDetailAdmin(admin.ModelAdmin):
    fieldsets = ((None, {'fields': ('description', 'created', 'updated')}),)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
    }
    list_display = ['description',]
    model = EducationDetail
    ordering = ('description',)
    readonly_fields = ('created', 'updated')
    search_fields = ('description',)


class FieldAdmin(admin.ModelAdmin):
    fieldsets = ((None, {'fields': ('category', 'created', 'updated')}),)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
    }
    list_display = ['category',]
    model = Field
    ordering = ('category',)
    readonly_fields = ('created', 'updated')
    search_fields = ('category',)


class GenderAdmin(admin.ModelAdmin):
    fieldsets = ((None, {'fields': ('category', 'created', 'updated')}),)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
    }
    list_display = ['category',]
    model = Gender
    ordering = ('category',)
    readonly_fields = ('created', 'updated')
    search_fields = ('category',)


class HeritageAdmin(admin.ModelAdmin):
    fieldsets = ((None, {'fields': ('category', 'created', 'updated')}),)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
    }
    list_display = ['category',]
    model = Heritage
    ordering = ('category',)
    readonly_fields = ('created', 'updated')
    search_fields = ('category',)


class InterestAdmin(admin.ModelAdmin):
    fieldsets = ((None, {'fields': ('category', 'created', 'updated')}),)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
    }
    list_display = ['category',]
    model = Interest
    ordering = ('category',)
    readonly_fields = ('created', 'updated')
    search_fields = ('category',)


class LocationDetailAdmin(admin.ModelAdmin):
    fieldsets = ((None, {'fields': ('description', 'created', 'updated')}),)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
    }
    list_display = ['description',]
    model = LocationDetail
    ordering = ('description',)
    readonly_fields = ('created', 'updated')
    search_fields = ('description',)


class MilitaryAdmin(admin.ModelAdmin):
    fieldsets = ((None, {'fields': ('category', 'created', 'updated')}),)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
    }
    list_display = ['category',]
    model = Military
    ordering = ('category',)
    readonly_fields = ('created', 'updated')
    search_fields = ('category',)


class ProviderAdmin(admin.ModelAdmin):
    fieldsets = (
        (('Contact'), {'fields': (
            'organization',
            'addressee',
            'email',
            'phone_number',
            'phone_number_ext',
        )}),
        (('Address'), {'fields': (
            'street',
            'city',
            'state',
            'zipcode',
        )}),
    )
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
    }
    list_display = ['organization', 'addressee', 'email',]
    model = Provider
    ordering = ('organization',)
    search_fields = ('organization', 'addressee', 'email', 'state',)


class ScholarshipAdmin(admin.ModelAdmin):
    fieldsets = (
        (('Details'), {'fields': (
            'name',
            'provider',
            'deadline',
            'description',
            'max_amount',
            'number_awards',
            'renewable',
            'website',
            'created',
            'updated',
        )}),
        (('Requirements'), {'fields': (
            'financial_need',
            'first_generation',
            'min_act',
            'min_sat',
            'min_gpa',
            'max_gpa',
            'writing',
        )}),
        (('Requirements Other Models'), {'fields': (
            'association',
            'citizenship',
            'college',
            'degree',
            'field',
            'disability',
            'gender',
            'heritage',
            'interest',
            'military',
        )}),
    )
    filter_horizontal = (
        'association',
        'citizenship',
        'college',
        'degree',
        'disability',
        'field',
        'gender',
        'heritage',
        'interest',
        'military',
    )
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size': '50'})},
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 3, 'cols': 100})},
    }
    inlines = [EducationScholarshipInline, LocationScholarshipInline]
    list_display = ['name', 'provider', 'deadline', 'max_amount',]
    model = Scholarship
    ordering = ('name', 'provider',)
    readonly_fields = ('created', 'updated',)
    search_fields = ('name', 'provider', 'deadline', 'max_amount',)


class ScholarshipStatusAdmin(admin.ModelAdmin):
    fieldsets = ((None, {'fields': (
        'user',
        'scholarship',
        'status',
        'created',
        'updated'
    )}),)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
    }
    list_display = ['status', 'scholarship', 'user']
    model = ScholarshipStatus
    ordering = ('user', 'scholarship',)
    readonly_fields = ('created', 'updated',)
    search_fields = ('user', 'scholarship', 'status',)


class StateAdmin(admin.ModelAdmin):
    fieldsets = ((None, {'fields': ('name', 'abbreviation', 'created', 'updated')}),)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
    }
    list_display = ['name', 'abbreviation',]
    model = State
    ordering = ('name',)
    readonly_fields = ('created', 'updated')
    search_fields = ('name', 'abbreviation',)


admin.site.register(Association, AssociationAdmin)
admin.site.register(Citizenship, CitizenshipAdmin)
admin.site.register(Degree, DegreeAdmin)
admin.site.register(Disability, DisabilityAdmin)
admin.site.register(EducationCategory, EducationCategoryAdmin)
admin.site.register(EducationDetail, EducationDetailAdmin)
admin.site.register(Field, FieldAdmin)
admin.site.register(Gender, GenderAdmin)
admin.site.register(Heritage, HeritageAdmin)
admin.site.register(Interest, InterestAdmin)
admin.site.register(LocationDetail, LocationDetailAdmin)
admin.site.register(Military, MilitaryAdmin)
admin.site.register(Provider, ProviderAdmin)
admin.site.register(Scholarship, ScholarshipAdmin)
admin.site.register(ScholarshipStatus, ScholarshipStatusAdmin)
admin.site.register(State, StateAdmin)
