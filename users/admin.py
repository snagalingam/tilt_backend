from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group
from django.forms import TextInput, Textarea
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
from users.models import AccountType, Action, DeletedAccount, Ethnicity, EthnicityUser, Income, Pronoun, PronounUser, Source, SourceUser


User = get_user_model()

################################################
### Inlines
################################################
class EthnicityUserInline(admin.StackedInline):
    extra = 0
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '20'})},
    }
    model = EthnicityUser


class PronounUserInline(admin.StackedInline):
    extra = 0
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '20'})},
    }
    model = PronounUser

class SourceUserInline(admin.StackedInline):
    extra = 0
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '20'})},
    }
    model = SourceUser


################################################
### Objects on Admin Panel
################################################
class AccountTypeAdmin(admin.ModelAdmin, DynamicArrayMixin):
    def account_type_count(self, obj):
        return obj.user_set.count()

    fieldsets = (
        (None, {'fields': ('type',)}),
    )
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '10'})},
    }
    list_display = ['type', 'account_type_count']
    model = AccountType
    ordering = ('type',)
    search_fields = ('type',)


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

    fieldsets = ((None, {'fields': ('ethnicity',)}),)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '10'})},
    }
    list_display = ['ethnicity', 'ethnicity_user_count']
    model = Ethnicity
    ordering = ('ethnicity', )
    search_fields = ('ethnicity',)


class IncomeAdmin(admin.ModelAdmin, DynamicArrayMixin):
    def user_income_count(self, obj):
        return obj.user_set.count()

    fieldsets = ((None, {'fields': ('category', 'description',)}),)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '10'})},
    }
    list_display = ['category', 'description', 'user_income_count']
    model = Income
    ordering = ('category',)
    search_fields = ('category', 'description',)


class PronounAdmin(admin.ModelAdmin, DynamicArrayMixin):
    def pronoun_user_count(self, obj):
        return obj.pronounuser_set.count()

    fieldsets = ((None, {'fields': ('pronoun',)}),)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '10'})},
    }
    list_display = ['pronoun', 'pronoun_user_count']
    model = Pronoun
    ordering = ('pronoun',)
    search_fields = ('pronoun',)



class SourceAdmin(admin.ModelAdmin, DynamicArrayMixin):
    def source_user_count(self, obj):
        return obj.sourceuser_set.count()

    fieldsets = ((None, {'fields': ('source',)}),)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '10'})},
    }
    list_display = ['source', 'source_user_count']
    model = Source
    ordering = ('source',)
    search_fields = ('source',)


class UserAdmin(UserAdmin, DynamicArrayMixin):
    fieldsets = (
        (('Contact Information'), {'fields': (
            'email',
            'first_name',
            'preferred_name',
            'last_name',
            'phone_number',
            'preferred_contact_method',
        )}),
        (('Account Information'), {'fields': (
            'account_type',
            'is_active',
            'is_verified',
            'is_onboarded',
            'is_test',
            'is_staff',
            'is_superuser',
        )}),
        (('Organizations'), {'fields': ('organization',)}),
        (('Other Information'), {'fields': (
            'high_school_grad_year',
            'gpa',
            'act_score',
            'sat_math',
            'sat_verbal',
            'efc',
            'income',
        )}),
    )
    filter_horizontal = ('organization',)
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size': '50'})},
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 3, 'cols': 100})},
    }
    inlines = [EthnicityUserInline, PronounUserInline, SourceUserInline,]
    list_display = [
        'email',
        'account_type',
        'is_active',
        'is_verified',
        'is_onboarded',
        'is_test',
        'is_staff',
        'is_superuser',
    ]
    model = User
    search_fields = (
        'email',
        'first_name',
        'preferred_name',
        'last_name',
        'account_type',
        'is_active',
        'is_verified',
        'is_onboarded',
        'is_test',
        'is_staff',
        'is_superuser',
    )
    ordering = ('email',)


admin.site.register(Action, ActionAdmin)
admin.site.register(DeletedAccount, DeletedAccountAdmin)
admin.site.register(Ethnicity, EthnicityAdmin)
admin.site.register(Income, IncomeAdmin)
admin.site.register(Pronoun, PronounAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(AccountType, AccountTypeAdmin)
