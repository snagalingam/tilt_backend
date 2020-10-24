from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from .models import CollegeStatus

from django.forms import TextInput, Textarea
from django.db import models

class CollegeStatusAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size': '50'})},
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 3, 'cols': 100})},
    }
    list_display = ['status', 'college', 'user', ]
    fieldsets = (
        (_('College Status Information'), {
            'fields': ('status', 'college', 'user', 'net_price')
        }),
    )

    search_fields = ('status', 'college', 'user',)
    ordering = ('status',)
    model = CollegeStatus

admin.site.register(CollegeStatus, CollegeStatusAdmin)
