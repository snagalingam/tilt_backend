from colleges.models import Budget, College, CollegeStatus, FieldOfStudy, Scorecard

from django.contrib import admin
from django.db import models
from django.forms import Textarea, TextInput
from django.utils.translation import gettext_lazy as _
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin


class BudgetAdmin(admin.ModelAdmin):
    fieldsets = (
        (('Information'), {
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
                'created',
                'updated'
            )
        }),
    )
    formfield_overrides = {models.IntegerField: {'widget': TextInput(attrs={'size': '50'})},}
    list_display = ['college_status']
    model = Budget
    ordering = ('college_status',)
    readonly_fields = ('created', 'updated')
    search_fields = ('college_status',)


class CollegeAdmin(admin.ModelAdmin, DynamicArrayMixin):
    fieldsets = (
        (('College Information'), {'fields': ('name', 'popularity_score',)}),
        (('Google Places Information'), {'fields': (
            'place_id',
            'address',
            'business_status',
            'description',
            'lat',
            'lng',
            'main_photo',
            'phone_number',
            'photos',
            'types',
            'url',
            'website',
        )}),
        (('Other Information'), {'fields': ('favicon','created', 'updated',)}),
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
    readonly_fields = ('created', 'updated')
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
                'user',
                'college',
                'status',
                'award_status',
                'in_state_tuition',
                'residency',
                'created',
                'updated'
            )
        }),
    )
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size': '50'})},
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
    }
    list_display = [
        'user',
        'college',
        'status',
        'award_status',
    ]
    model = CollegeStatus
    ordering = ('status', 'college', 'user',)
    readonly_fields = ('created', 'updated')
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
    search_fields = ('cip_title', 'college', 'credential_level',)


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
admin.site.register(College, CollegeAdmin)
admin.site.register(CollegeStatus, CollegeStatusAdmin)
admin.site.register(FieldOfStudy, FieldOfStudyAdmin)
admin.site.register(Scorecard, ScorecardAdmin)
