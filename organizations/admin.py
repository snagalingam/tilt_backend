from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Organization

from django.forms import TextInput, Textarea
from django.db import models

class OrganizationAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size': '50'})},
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 3, 'cols': 100})},
    }
    list_display = ['name', 'tilt_partnership', 'address', ]
    list_editable = ['tilt_partnership', ]
    fieldsets = (
        (_('Partnership'), {'fields': ('tilt_partnership',)}),
        (_('Contact Information'), {
            'fields': ('name', 'address', 'phone_number',)
        }),
        (_('Detailed Information'), {
            'fields': ('business_status', 'types', 'website',)
        }),
        (_('Google Information'), {
            'fields': ('place_id', 'lat', 'lng', 'url',)
        })
    )

    search_fields = ('name', 'tilt_partnership', 'address',)
    ordering = ('name',)
    model = Organization

admin.site.register(Organization, OrganizationAdmin)
