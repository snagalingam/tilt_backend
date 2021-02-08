from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group
from django.forms import TextInput, Textarea
from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import Action, DeletedAccount, Ethnicity, EthnicityUser, Income, Pronoun, PronounUser, Source, SourceUser, UserCategory


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
class ActionAdmin(admin.ModelAdmin):
    fieldsets = ((None, {'fields': ('user', 'description', 'timestamp',)}),)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '10'})},
    }
    list_display = ['user', 'description', 'timestamp']
    model = Action
    ordering = ('timestamp',)
    search_fields = ('user__email', 'description', 'timestamp',)


class DeletedAccountAdmin(admin.ModelAdmin):
    fieldsets = ((None, {'fields': ('date', 'accounts',)}),)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '10'})},
    }
    list_display = ['date', 'accounts',]
    model = DeletedAccount
    ordering = ('date',)
    search_fields = ('date', 'accounts',)


class EthnicityAdmin(admin.ModelAdmin):
    def ethnicity_user_count(self, obj):
        return obj.ethnicityuser_set.count()

    fieldsets = (
        (None, {'fields': ('category', 'description', 'created', 'updated')}),
    )
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '10'})},
    }
    list_display = ['category', 'description', 'ethnicity_user_count']
    model = Ethnicity
    ordering = ('category',)
    readonly_fields = ('created', 'updated')
    search_fields = ('category',)


class IncomeAdmin(admin.ModelAdmin):
    def user_income_count(self, obj):
        return obj.user_set.count()

    fieldsets = ((None, {'fields': ('category', 'description', 'created', 'updated',)}),)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '10'})},
    }
    list_display = ['category', 'description', 'user_income_count']
    model = Income
    ordering = ('category',)
    readonly_fields = ('created', 'updated',)
    search_fields = ('category', 'description',)


class PronounAdmin(admin.ModelAdmin):
    def pronoun_user_count(self, obj):
        return obj.pronounuser_set.count()

    fieldsets = ((None, {'fields': ('category', 'created', 'updated',)}),)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '10'})},
    }
    list_display = ['category', 'pronoun_user_count']
    model = Pronoun
    ordering = ('category',)
    readonly_fields = ('created', 'updated',)
    search_fields = ('category',)


class SourceAdmin(admin.ModelAdmin):
    def source_user_count(self, obj):
        return obj.sourceuser_set.count()

    fieldsets = ((None, {'fields': ('category', 'created', 'updated')}),)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '10'})},
    }
    list_display = ['category', 'source_user_count']
    model = Source
    ordering = ('category',)
    readonly_fields = ('created', 'updated',)
    search_fields = ('category',)


class UserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2',),
        }),
    )
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
            'user_category',
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
            'created',
            'updated',
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
        'user_category',
        'is_active',
        'is_verified',
        'is_onboarded',
        'is_test',
        'is_staff',
        'is_superuser',
    ]
    model = User
    readonly_fields = ('created', 'updated',)
    search_fields = (
        'email',
        'first_name',
        'preferred_name',
        'last_name',
        'user_category__category',
        'is_active',
        'is_verified',
        'is_onboarded',
        'is_test',
        'is_staff',
        'is_superuser',
    )
    ordering = ('email',)


class UserCategoryAdmin(admin.ModelAdmin):
    def user_category_count(self, obj):
        return obj.user_set.count()

    fieldsets = (
        (None, {'fields': ('category', 'created', 'updated',)}),
    )
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '10'})},
    }
    list_display = ['category', 'user_category_count']
    model = UserCategory
    ordering = ('category',)
    readonly_fields = ('created', 'updated',)
    search_fields = ('category',)


admin.site.register(Action, ActionAdmin)
admin.site.register(DeletedAccount, DeletedAccountAdmin)
admin.site.register(Ethnicity, EthnicityAdmin)
admin.site.register(Income, IncomeAdmin)
admin.site.register(Pronoun, PronounAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(UserCategory, UserCategoryAdmin)
admin.site.unregister(Group)
