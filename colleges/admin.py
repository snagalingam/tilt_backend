from colleges.models import College, CollegeStatus, FieldOfStudy, Ipeds, Scorecard
from django.contrib import admin
from django.db import models
from django.forms import Textarea, TextInput
from django.utils.translation import gettext_lazy as _
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
from financial_aid.models import AidFinalData, AidRawData


################################################
# Inline
################################################
class AidFinalData(admin.StackedInline):
    model = AidFinalData
    extra = 0
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '100'})},
    }

class AidRawData(admin.StackedInline):
    model = AidRawData
    extra = 0
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '100'})},
    }

################################################
# Objects on admin panel
################################################
class CollegeAdmin(admin.ModelAdmin, DynamicArrayMixin):
    fieldsets = (
        (('College Information'), {'fields': ('name', 'scorecard_unit_id', 'show', 'popularity_score',)}),
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
    list_display = ['name', 'show', 'scorecard_unit_id', 'popularity_score', 'website']
    list_editable = ['show',]
    model = College
    ordering = ('name',)
    readonly_fields = ('created', 'updated')
    search_fields = (
        'show',
        'name',
        'popularity_score',
        'scorecard_unit_id',
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
                'net_price',
                'residency',
            )
        }),
        (('Award Totals'), {
            'fields': (
                'award_costs_missing',
                'award_total_costs',
                'award_total_grants',
                'award_net_price',
                'most_affordable',
            )
        }),
        (('Budget'), {
            'fields': (
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
        (('Timestamp Fields'), {
            'fields': (
                'created',
                'updated',
            )
        }),
    )
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size': '50'})},
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
    }
    inlines = [AidRawData, AidFinalData]
    list_display = [
        'user',
        'college',
        'status',
        'award_status',
    ]
    model = CollegeStatus
    ordering = ('user', 'status', 'college',)
    readonly_fields = ('created', 'updated')
    search_fields = ('user__email',)


class FieldOfStudyAdmin(admin.ModelAdmin, DynamicArrayMixin):
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size': '50'})},
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 3, 'cols': 100})},
    }
    list_display = ['cip_title', 'college', 'credential_level', 'show']
    model = FieldOfStudy
    ordering = ('college', 'credential_level',)
    search_fields = ('cip_title', 'college', 'credential_level',)


class IpedsAdmin(admin.ModelAdmin):
    list_display = ['unit_id', 'college', 'updated',]
    model = Ipeds
    ordering = ('unit_id',)
    search_fields = ('unit_id', 'updated')
    readonly_fields = ('created', 'updated')


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


admin.site.register(College, CollegeAdmin)
admin.site.register(CollegeStatus, CollegeStatusAdmin)
admin.site.register(FieldOfStudy, FieldOfStudyAdmin)
admin.site.register(Ipeds, IpedsAdmin)
admin.site.register(Scorecard, ScorecardAdmin)
