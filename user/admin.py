from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
from user.models import DeletedAccount, Action


User = get_user_model()

################################################
### Inline
################################################
class ActionInline(admin.TabularInline):
    extra = 0
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '20'})},
    }
    model = Action


################################################
### Admin Panel
################################################
class ActionAdmin(admin.ModelAdmin, DynamicArrayMixin):
    fieldsets = ((None, {'fields': ('user', 'description', 'timestamp',)}),)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '10'})},
    }
    list_display = ['user', 'description', 'timestamp']
    model = Action
    ordering = ('timestamp',)
    search_fields = ('user__email', 'description', 'timestamp',)


class DeletedAccountAdmin(admin.ModelAdmin, DynamicArrayMixin):
    fieldsets = ((None, {'fields': ('date', 'accounts',)}),)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '10'})},
    }
    list_display = ['date', 'accounts',]
    model = DeletedAccount
    ordering = ('date',)
    search_fields = ('date', 'accounts',)


class UserAdmin(UserAdmin, DynamicArrayMixin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    fieldsets = (
        (None, {'fields': ('email', 'password', 'phone_number', 'preferred_contact_method')}),
        (('Personal Information'), {'fields': (
            'first_name',
            'last_name',
            'preferred_name',
            'pronouns')
        }),
        (('Account Status'), {'fields': (
            'is_staff',
            'is_superuser',
            'is_active',
            'is_verified',
            'is_onboarded',
            'is_test',
            'user_type')
        }),
        (('Background Information'), {'fields': ('ethnicity', 'found_from')}),
        (('Organization Information'), {'fields': ('organization')}),
        (('Academic Information'), {'fields': (
            'gpa',
            'act_score',
            'sat_math',
            'sat_verbal',
            'high_school_grad_year'
        )}),
        (('Financial Information'), {'fields': ('efc', 'income_quintile')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    filter_horizontal = ('organization',)
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size': '50'})},
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 3, 'cols': 100})},
    }
    inlines = [ActionInline]
    list_display = [
        'email',
        'is_staff',
        'is_superuser',
        'is_active',
        'is_verified',
        'is_onboarded',
        'is_test'
    ]
    list_editable = [
        'is_staff',
        'is_superuser',
        'is_active',
        'is_verified',
        'is_onboarded',
        'is_test'
    ]
    model = User
    search_fields = (
        'email',
        'first_name',
        'last_name',
        'is_staff',
        'is_superuser',
        'is_active',
        'is_verified',
        'is_onboarded'
    )
    ordering = ('email',)


admin.site.register(User, UserAdmin)
admin.site.register(DeletedAccount, DeletedAccountAdmin)
admin.site.register(Action, ActionAdmin)
