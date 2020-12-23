from .models import Organization
from django.contrib import admin
from django.db import models
from django.forms import Textarea, TextInput
from django.utils.translation import gettext_lazy as _
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin


class OrganizationAdmin(admin.ModelAdmin, DynamicArrayMixin):
    fieldsets = (
        (('Partnership'), {'fields': ('partner',)}),
        (('Contact Information'), {'fields': ('name', 'address', 'phone_number',)}),
        (('Detailed Information'), {'fields': ('business_status', 'types', 'website',)}),
        (('Google Information'), {'fields': ('place_id', 'lat', 'lng', 'url',)}),
    )
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size': '50'})},
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 3, 'cols': 100})},
    }
    list_display = ['name', 'partner', 'address', ]
    list_editable = ['partner', ]
    model = Organization
    ordering = ('name',)
    search_fields = ('name', 'partner', 'address',)


admin.site.register(Organization, OrganizationAdmin)
