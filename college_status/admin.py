from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from .models import Status

from django.forms import TextInput, Textarea
from django.db import models

class StatusAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size': '50'})},
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
    }
    list_display = ['status', 'college', 'user', 'net_price', 'award_uploaded', 'reviewed', 'user_notified']
    list_editable = ['reviewed', ]
    
    fieldsets = (
        (_('College Status Information'), {
            'fields': ('status', 'college', 'user', 'net_price', 'award_uploaded', 'reviewed', 'user_notified')
        }),
    )

    search_fields = ('status', 'college__name', 'user__email',)
    ordering = ('status', 'college__name', 'user__email',)
    model = Status

admin.site.register(Status, StatusAdmin)
