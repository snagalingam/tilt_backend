# from django.contrib import admin
# from .models import Organization

# admin.site.register(Organization)

from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from organizations.models import Organization

class OrganizationAdmin(admin.ModelAdmin):
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
