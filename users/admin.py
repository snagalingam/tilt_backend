from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from organizations.models import Organization

from .forms import CustomUserChangeForm, CustomUserCreationForm

CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['email', 'first_name', 'last_name', 'is_staff']
    fieldsets = (
        (_('Account info'), {'fields': ('email', 'password', 'user_type')}),
        (_('Personal info'), {
            'fields': ('first_name', 'last_name', 'preferred_name', 'pronouns', 'is_verified')
        }),
        (_('Academic info'), {
            'fields': ('highschool_graduation_year', 'gpa', 'act_score', 'sat_score')
        }),
        (_('Organizations'), {
            'fields': ('organization',)
        }),
        (_('Background info'), {
            'fields': ('ethnicity', 'income_quintile', 'efc', 'found_from')
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'first_name', 'last_name', 'preferred_name')
    ordering = ('email',)

    model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)
