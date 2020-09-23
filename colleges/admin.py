from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from .models import College

from django.forms import TextInput, Textarea
from django.db import models

class CollegeAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size': '50'})},
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 3, 'cols': 100})},
    }
    list_display = ['name', 'website', 'description']
    fieldsets = (
        (None, {'fields': ('description',)}),
        (_('College Information'), {
            'fields': ('name', 'address', 'phone_number', 'website',)
        }),
        (_('Scorcard Information'), {
            'fields': ('unit_id', 'ope_id',)
        }),
        (_('Google Places Information'), {
            'fields': ('place_id', 'lat', 'lng', 'url',)
        }),
        (_('Other Information'), {
            'fields': ('types', 'main_photo', 'photos',)
        }),
    )

    search_fields = ('name', 'unit_id', 'ope_id',)
    ordering = ('name',)
    model = College


admin.site.register(College, CollegeAdmin)
