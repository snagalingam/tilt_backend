from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from .models import Budget

from django.forms import TextInput, Textarea
from django.db import models

class BudgetAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size': '50'})},
    }
    list_display = ['college_status',]

    fieldsets = (
        (None, {
            'fields': (
                'college_status', 'work_study', 'job', 'savings', 'family', 
                'other_scholarships', 'loan_subsideized', 'loan_unsubsideized', 
                'loan_plus', 'loan_private', 'loan_school',)
        }),
    )

    search_fields = ('college_status__pk',)
    ordering = ('college_status__pk',)
    model = Budget

admin.site.register(Budget, BudgetAdmin)
