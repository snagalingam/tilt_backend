from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from django.forms import TextInput, Textarea
from django.db import models
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
from .models import DeletedAccount, Action, Pronoun, PronounUser, Source, SourceUser, Type, Income, Ethnicity, EthnicityUser
CustomUser = get_user_model()

# class PronounAdmin(admin.ModelAdmin, DynamicArrayMixin):

#     # def pronoun_count(self, obj):

#     #     return obj.data_set.count()

#     formfield_overrides = {
#         models.CharField: {'widget': TextInput(attrs={'size': '10'})},
#     }
#     list_display = ['pronoun',]

#     fieldsets = (
#         (None, {'fields': ('pronoun', )}),
#     )

#     search_fields = ('date', 'accounts',)
#     ordering = ('date',)

#     model = Pronoun

# class PronounUserAdmin(admin.ModelAdmin, DynamicArrayMixin):
#     formfield_overrides = {
#         models.CharField: {'widget': TextInput(attrs={'size': '10'})},
#     }
#     list_display = ['date', 'accounts',]

#     fieldsets = (
#         (None, {'fields': ('date', 'accounts',)}),
#     )

#     search_fields = ('date', 'accounts',)
#     ordering = ('date',)

#     model = PronounUser

# class SourceAdmin(admin.ModelAdmin, DynamicArrayMixin):
#     formfield_overrides = {
#         models.CharField: {'widget': TextInput(attrs={'size': '10'})},
#     }
#     list_display = ['date', 'accounts',]

#     fieldsets = (
#         (None, {'fields': ('date', 'accounts',)}),
#     )

#     search_fields = ('date', 'accounts',)
#     ordering = ('date',)

#     model = Source

# class SourceUserAdmin(admin.ModelAdmin, DynamicArrayMixin):
#     formfield_overrides = {
#         models.CharField: {'widget': TextInput(attrs={'size': '10'})},
#     }
#     list_display = ['date', 'accounts',]

#     fieldsets = (
#         (None, {'fields': ('date', 'accounts',)}),
#     )

#     search_fields = ('date', 'accounts',)
#     ordering = ('date',)

#     model = SourceUser

# class TypeAdmin(admin.ModelAdmin, DynamicArrayMixin):
#     formfield_overrides = {
#         models.CharField: {'widget': TextInput(attrs={'size': '10'})},
#     }
#     list_display = ['date', 'accounts',]

#     fieldsets = (
#         (None, {'fields': ('date', 'accounts',)}),
#     )

#     search_fields = ('date', 'accounts',)
#     ordering = ('date',)

#     model = Type

# class IncomeAdmin(admin.ModelAdmin, DynamicArrayMixin):
#     formfield_overrides = {
#         models.CharField: {'widget': TextInput(attrs={'size': '10'})},
#     }
#     list_display = ['date', 'accounts',]

#     fieldsets = (
#         (None, {'fields': ('date', 'accounts',)}),
#     )

#     search_fields = ('date', 'accounts',)
#     ordering = ('date',)

#     model = Income

# class EthnicityAdmin(admin.ModelAdmin, DynamicArrayMixin):
#     formfield_overrides = {
#         models.CharField: {'widget': TextInput(attrs={'size': '10'})},
#     }
#     list_display = ['date', 'accounts',]

#     fieldsets = (
#         (None, {'fields': ('date', 'accounts',)}),
#     )

#     search_fields = ('date', 'accounts',)
#     ordering = ('date',)

#     model = Ethnicity

# class EthnicityUserAdmin(admin.ModelAdmin, DynamicArrayMixin):
#     formfield_overrides = {
#         models.CharField: {'widget': TextInput(attrs={'size': '10'})},
#     }
#     list_display = ['date', 'accounts',]

#     fieldsets = (
#         (None, {'fields': ('date', 'accounts',)}),
#     )

#     search_fields = ('date', 'accounts',)
#     ordering = ('date',)

#     model = EthnicityUser

class DeletedAccountAdmin(admin.ModelAdmin, DynamicArrayMixin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '10'})},
    }
    list_display = ['date', 'accounts',]

    fieldsets = (
        (None, {'fields': ('date', 'accounts',)}),
    )

    search_fields = ('date', 'accounts',)
    ordering = ('date',)

    model = DeletedAccount

class ActionAdmin(admin.ModelAdmin, DynamicArrayMixin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '10'})},
    }
    list_display = ['user', 'description', 'timestamp']

    fieldsets = (
        (None, {'fields': ('user', 'description', 'timestamp',)}),
    )

    search_fields = ('user__email', 'description', 'timestamp',)
    ordering = ('timestamp',)

    model = Action

class ActionInline(admin.TabularInline):
    model = Action
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '20'})},
    }
    extra = 0

class CustomUserAdmin(UserAdmin, DynamicArrayMixin):
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size': '50'})},
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 3, 'cols': 100})},
    }
    list_display = ['email', 'is_staff', 'is_superuser',
                    'is_active', 'is_verified', 'is_onboarded', 'is_test_account']
    list_editable = ['is_staff', 'is_superuser',
                     'is_active', 'is_verified', 'is_onboarded', 'is_test_account']
    filter_horizontal = ('organization',) 
    
    fieldsets = (
        (None, {'fields': ('email', 'password', 'phone_number', 'preferred_contact_method')}),
        (_('Personal Information'), {
            'fields': ('first_name', 'last_name', 'preferred_name', 'pronouns')
        }),
        (_('Account Status'), {
            'fields': ('is_staff', 'is_superuser', 'is_active', 'is_verified', 'is_onboarded', 'is_test_account', 'user_type')
        }),
        (_('Background Information'), {
            'fields': ('ethnicity', 'found_from'),
        }),
        (_('Organization Information'), {
            'fields': ('organization',),
        }),
        (_('Academic Information'), {
            'fields': ('gpa', 'act_score', 'sat_math', 'sat_verbal', 'high_school_grad_year')
        }),
        (_('Financial Information'), {
            'fields': ('efc', 'income_quintile',)
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    
    inlines = [ActionInline]
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
admin.site.register(Action, ActionAdmin)
admin.site.register(DeletedAccount, DeletedAccountAdmin)
# admin.site.register(Pronoun, PronounAdmin)
# admin.site.register(PronounUser, PronounUserAdmin)
# admin.site.register(Source, SourceAdmin)
# admin.site.register(SourceUser, SourceUserAdmin)
# admin.site.register(Type, TypeAdmin)
# admin.site.register(Income, IncomeAdmin)
# admin.site.register(Ethnicity, EthnicityAdmin)
# admin.site.register(EthnicityUser, EthnicityUserAdmin)