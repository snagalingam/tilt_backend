from .models import Budget, College, CollegeStatus, FieldOfStudy, Scorecard

from django.contrib import admin
from django.db import models
from django.forms import Textarea, TextInput
from django.utils.translation import gettext_lazy as _
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin


class BudgetAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'college_status',
                'work_study',
                'job',
                'savings',
                'family',
                'other_scholarships',
                'loan_subsidized',
                'loan_unsubsidized',
                'loan_plus',
                'loan_private',
                'loan_school',
            )
        }),
    )
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size': '50'})},
    }
    list_display = ['college_status']
    model = Budget
    ordering = ('college_status',)
    search_fields = ('college_status',)

class CollegeAdmin(admin.ModelAdmin, DynamicArrayMixin):
    fieldsets = (
        (None, {'fields': ('description', 'popularity_score')}),
        (('College Information'), {
            'fields': ('name', 'address', 'phone_number', 'website', 'business_status')
        }),
        (('Scorcard Information'), {
            'fields': ('unit_id', 'ope_id')
        }),
        (('Google Places Information'), {
            'fields': ('place_id', 'lat', 'lng', 'url', 'favicon')
        }),
        (('Other Information'), {
            'fields': ('types', 'main_photo', 'photos')
        }),
    )
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size': '50'})},
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 3, 'cols': 100})},
    }
    list_display = ['name', 'website', 'popularity_score', 'description',]
    list_editable = ['description',]
    model = College
    ordering = ('name',)
    search_fields = (
        'name',
        'unit_id',
        'ope_id',
        'website',
        'popularity_score',
        'description',
        'favicon',
        'types',
    )


class CollegeStatusAdmin(admin.ModelAdmin):
    fieldsets = (
        (('College Status Information'), {
            'fields': (
                'status',
                'college',
                'user',
                'net_price',
                'award_uploaded',
                'award_reviewed',
                'user_notified',
            )
        }),
    )
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size': '50'})},
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
    }
    list_display = [
        'status',
        'college',
        'user',
        'net_price',
        'award_uploaded',
        'award_reviewed',
        'user_notified',
    ]
    list_editable = ['award_reviewed',]
    model = CollegeStatus
    ordering = ('status', 'college', 'user',)
    search_fields = ('status', 'college', 'user',)


class FieldOfStudyAdmin(admin.ModelAdmin, DynamicArrayMixin):
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size': '50'})},
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 3, 'cols': 100})},
    }
    list_display = ['cip_title', 'college', 'credential_level',]
    model = FieldOfStudy
    ordering = ('college', 'credential_level',)
    search_fields = ('cip_title', 'college__name', 'credential_level',)


class ScorecardAdmin(admin.ModelAdmin, DynamicArrayMixin):
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size': '50'})},
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 3, 'cols': 100})},
    }
    list_display = ['name', 'city', 'state', 'zipcode',]
    model = Scorecard
    ordering = ('name',)
    search_fields = ('name', 'unit_id', 'ope_id',)


admin.site.register(Budget, BudgetAdmin)
admin.site.register(CollegeStatus, CollegeStatusAdmin)
admin.site.register(FieldOfStudy, FieldOfStudyAdmin)
admin.site.register(Scorecard, ScorecardAdmin)
admin.site.register(Status, StatusAdmin)
