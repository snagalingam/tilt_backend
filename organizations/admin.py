from django.contrib import admin
from django.db import models
from django.forms import Textarea, TextInput
from organizations.models import Organization


class OrganizationAdmin(admin.ModelAdmin):
    fieldsets = (
        (('Basic Information'), {'fields': (
            'name',
            'place_id',
            'partner',
        )}),
        (('Detailed Information'), {'fields': (
            'address',
            'business_status',
            'icon',
            'lat',
            'lng',
            'phone_number',
            'types',
            'url',
            'website',
            'created',
            'updated'
        )}),
    )
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size': '50'})},
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 3, 'cols': 100})},
    }
    list_display = ['name', 'partner', 'address',]
    list_editable = ['partner',]
    model = Organization
    ordering = ('name',)
    readonly_fields = ('created', 'updated',)
    search_fields = ('name', 'partner', 'address',)


admin.site.register(Organization, OrganizationAdmin)
