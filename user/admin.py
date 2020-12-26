from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group
from django.forms import TextInput, Textarea
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
from user.models import Action, DeletedAccount, Ethnicity, EthnicityUser, Income, Pronoun, PronounUser, Source, SourceUser, UserType


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


class EthnicityAdmin(admin.ModelAdmin, DynamicArrayMixin):

    def ethnicity_user_count(self, obj):
        return obj.ethnicityuser_set.count()

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '10'})},
    }
    list_display = ['ethnicity', 'ethnicity_user_count']

    fieldsets = (
        (None, {'fields': ('ethnicity', )}),
    )

    search_fields = ('ethnicity', )
    ordering = ('ethnicity', )
    model = Ethnicity


class EthnicityUserAdmin(admin.ModelAdmin, DynamicArrayMixin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '10'})},
    }
    list_display = ['user', 'ethnicity', 'other_value', ]

    fieldsets = (
        (None, {'fields': ('user', 'ethnicity', 'other_value', )}),
    )

    search_fields = ('user', 'ethnicity',)
    ordering = ('user',)
    model = EthnicityUser


class IncomeAdmin(admin.ModelAdmin, DynamicArrayMixin):

    def user_income_count(self, obj):
        return obj.user_set.count()

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '10'})},
    }
    list_display = ['category', 'description', 'user_income_count']

    fieldsets = (
        (None, {'fields': ('category', 'description', )}),
    )

    search_fields = ('category', 'description', )
    ordering = ('category', )
    model = Income

class PronounAdmin(admin.ModelAdmin, DynamicArrayMixin):

    def pronoun_user_count(self, obj):
        return obj.pronounuser_set.count()

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '10'})},
    }
    list_display = ['pronoun', 'pronoun_user_count']

    fieldsets = (
        (None, {'fields': ('pronoun', )}),
    )

    search_fields = ('pronoun', )
    ordering = ('pronoun', )
    model = Pronoun


class PronounUserAdmin(admin.ModelAdmin, DynamicArrayMixin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '10'})},
    }
    list_display = ['user', 'pronoun', 'other_value']

    fieldsets = (
        (None, {'fields': ('user', 'pronoun', 'other_value', )}),
    )

    search_fields = ('user', 'pronoun', )
    ordering = ('user', )
    model = PronounUser


class SourceAdmin(admin.ModelAdmin, DynamicArrayMixin):

    def source_user_count(self, obj):
        return obj.sourceuser_set.count()

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '10'})},
    }
    list_display = ['source', 'source_user_count']

    fieldsets = (
        (None, {'fields': ('source', )}),
    )

    search_fields = ('source', )
    ordering = ('source', )
    model = Source


class SourceUserAdmin(admin.ModelAdmin, DynamicArrayMixin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '10'})},
    }
    list_display = ['user', 'source']

    fieldsets = (
        (None, {'fields': ('user', 'source', 'other_value', )}),
    )

    search_fields = ('user', 'source', )
    ordering = ('user', )
    model = SourceUser


class UserAdmin(UserAdmin, DynamicArrayMixin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2',),
        }),
    )
    fieldsets = (
        (None, {'fields': ('email', 'password', 'phone_number', 'preferred_contact_method',)}),
        (('Personal Information'), {'fields': (
            'first_name',
            'last_name',
            'preferred_name',
            'pronouns',
        )}),
        (('Account Status'), {'fields': (
            'is_staff',
            'is_superuser',
            'is_active',
            'is_verified',
            'is_onboarded',
            'is_test',
            'user_type',
        )}),
        (('Background Information'), {'fields': ('ethnicity', 'found_from',)}),
        (('Organization Information'), {'fields': ('organization',)}),
        (('Academic Information'), {'fields': (
            'gpa',
            'act_score',
            'sat_math',
            'sat_verbal',
            'high_school_grad_year',
        )}),
        (('Financial Information'), {'fields': ('efc', 'income_quintile',)}),
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
        'is_test',
    ]
    list_editable = [
        'is_staff',
        'is_superuser',
        'is_active',
        'is_verified',
        'is_onboarded',
        'is_test',
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
        'is_onboarded',
    )
    ordering = ('email',)


class UserTypeAdmin(admin.ModelAdmin, DynamicArrayMixin):

    def user_type_count(self, obj):
        return obj.user_set.count()

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '10'})},
    }
    list_display = ['user_type', 'user_type_count']

    fieldsets = (
        (None, {'fields': ('user_type',)}),
    )

    search_fields = ('user_type', )
    ordering = ('user_type', )
    model = UserType


admin.site.register(Action, ActionAdmin)
admin.site.register(DeletedAccount, DeletedAccountAdmin)
admin.site.register(Ethnicity, EthnicityAdmin)
admin.site.register(EthnicityUser, EthnicityUserAdmin)
admin.site.register(Income, IncomeAdmin)
admin.site.register(Pronoun, PronounAdmin)
admin.site.register(PronounUser, PronounUserAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(SourceUser, SourceUserAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(UserType, UserTypeAdmin)