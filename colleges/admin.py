from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from .models import College, Scorecard, FieldOfStudy, CollegeStatus, Budget

from django.forms import TextInput, Textarea
from django.db import models
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

class CollegeAdmin(admin.ModelAdmin, DynamicArrayMixin):
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size': '50'})},
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 3, 'cols': 100})},
    }
    list_display = ['name', 'website', 'popularity_score', 'description']
    list_editable = ['description',]
    
    fieldsets = (
        (None, {'fields': ('description', 'popularity_score',)}),
        (_('College Information'), {
            'fields': ('name', 'address', 'phone_number', 'website', 'business_status')
        }),
        (_('Scorcard Information'), {
            'fields': ('unit_id', 'ope_id',)
        }),
        (_('Google Places Information'), {
            'fields': ('place_id', 'lat', 'lng', 'url', 'favicon')
        }),
        (_('Other Information'), {
            'fields': ('types', 'main_photo', 'photos',)
        }),
    )
    search_fields = ('name', 'unit_id', 'ope_id', 'website', 'popularity_score', 
        'description', 'favicon', 'types',)
    ordering = ('name',)
    model = College

class ScorecardAdmin(admin.ModelAdmin, DynamicArrayMixin):
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size': '50'})},
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 3, 'cols': 100})},
    }
    list_display = ['name', 'city', 'state', 'zipcode']
    search_fields = ('name', 'unit_id', 'ope_id',)
    ordering = ('name',)
    model = Scorecard

class FieldOfStudyAdmin(admin.ModelAdmin, DynamicArrayMixin):
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size': '50'})},
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 3, 'cols': 100})},
    }
    list_display = ['cip_title', 'college', 'credential_level', ]
    search_fields = ('cip_title', 'college', 'credential_level',)
    ordering = ('college', 'credential_level',)
    model = FieldOfStudy

class CollegeStatusAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size': '50'})},
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
    }
    list_display = ['status', 'college', 'user', 'net_price', 'award_uploaded', 
        'award_reviewed', 'user_notified', 'residency', 'in_state_tuition']
    list_editable = ['award_reviewed', ]

    fieldsets = (
        (_('College Status Information'), {
            'fields': ('status', 'college', 'user', 'net_price', 'award_uploaded', 
            'award_reviewed', 'user_notified')
        }),
    )

    search_fields = ('status', 'college', 'user',)
    ordering = ('status', 'college', 'user',)
    model = CollegeStatus

class BudgetAdmin(admin.ModelAdmin):

    def user(self, obj):
        return obj.college_status.user

    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size': '50'})},
    }
    list_display = ['college_status', 'user']

    fieldsets = (
        (None, {
            'fields': (
                'college_status', 'work_study', 'job', 'savings', 'family', 
                'other_scholarships', 'loan_subsidized', 'loan_unsubsidized', 
                'loan_plus', 'loan_private', 'loan_school',)
        }),
    )

    search_fields = ('college_status',)
    ordering = ('college_status',)
    model = Budget


admin.site.register(College, CollegeAdmin)
admin.site.register(Scorecard, ScorecardAdmin)
admin.site.register(FieldOfStudy, FieldOfStudyAdmin)
admin.site.register(CollegeStatus, CollegeStatusAdmin)
admin.site.register(Budget, BudgetAdmin) 