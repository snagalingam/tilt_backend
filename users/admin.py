from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from django.forms import TextInput, Textarea
from django.db import models
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin, DynamicArrayMixin):
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size': '50'})},
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 3, 'cols': 100})},
    }
    list_display = ['email', 'is_staff', 'is_superuser',
                    'is_active', 'is_verified', 'is_onboarded']
    list_editable = ['is_staff', 'is_superuser',
                     'is_active', 'is_verified', 'is_onboarded']
    filter_horizontal = ('organization',) 
    
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        (_('Personal Information'), {
            'fields': ('first_name', 'last_name', 'preferred_name', 'pronouns')
        }),
        (_('Account Status'), {
            'fields': ('is_staff', 'is_superuser', 'is_active', 'is_verified', 'is_onboarded', 'user_type')
        }),
        (_('Background Information'), {
            'fields': ('ethnicity', 'found_from'),
        }),
        (_('Organization Information'), {
            'fields': ('organization',),
        }),
        (_('Academic Information'), {
            'fields': ('gpa', 'act_score', 'sat_score', 'high_school_grad_year')
        }),
        (_('Financial Information'), {
            'fields': ('efc', 'income_quintile',)
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'first_name', 'last_name', 'is_staff',
                     'is_superuser', 'is_active', 'is_verified', 'is_onboarded')
    ordering = ('email',)

    model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)
