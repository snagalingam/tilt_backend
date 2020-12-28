import datetime
from django.conf import settings
from django.contrib.auth.base_user import (
    AbstractBaseUser,
    BaseUserManager,
)
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django_better_admin_arrayfield.models.fields import ArrayField
from organizations.models import Organization


DEFAULT_CHAR_TEXT = ""
DEFAULT_ETHNICITY_ID = 1
DEFAULT_INCOME_ID = 1
DEFAULT_PRONOUN_ID = 1
DEFAULT_SOURCE_ID = 1
DEFAULT_USER_ID = 1
DEFAULT_USER_TYPE_ID = 1


################################################
### Foreign Key Fields in User
################################################
class Income(models.Model):
    category = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'income'
        verbose_name_plural = 'incomes'

    def __str__(self):
        return self.category


class AccountType(models.Model):
    type = models.CharField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "account type"
        verbose_name_plural = "account types"

    def __str__(self):
        return self.type


################################################
### User Model
################################################
class UserManager(BaseUserManager):
    """ User manager for User that allows users to be created """

    use_in_migrations = True

    def _create_user(self, email, first_name=None, last_name=None, password=None, **extra_fields):
        if not email:
            raise ValueError("Email must be provided")
        email = self.normalize_email(email)
        user = self.model(
            email=email, first_name=first_name, last_name=last_name, **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, first_name=None, last_name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, first_name, last_name, password, **extra_fields)

    def create_superuser(
        self, email, first_name, last_name, password=None, **extra_fields
    ):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, first_name, last_name, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """ User model that extends AbstractBaseUser and PermissionsMixin """

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]
    CONTACT_METHOD_CHOICES = (
        ("text", "text"),
        ("email", "email")
    )

    # contact information
    email = models.EmailField(_("Email Address"),
        unique=True,
        error_messages={
            "unique": _("A user is already registered with this email address"),
        },
    )
    first_name = models.CharField(_("First Name"), max_length=255)
    preferred_name = models.CharField(
        _("Preferred Name"),
        blank=True,
        max_length=255
    )
    last_name = models.CharField(_("Last Name"), max_length=255)
    phone_number = models.CharField(
        _("Phone Number"),
        blank=True,
        max_length=15
    )
    preferred_contact_method = models.CharField(
        _("Preferred Contact Method"),
        blank=True,
        choices=CONTACT_METHOD_CHOICES,
        max_length=255,
    )

    # account information
    account_type = models.ForeignKey(
        AccountType,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    is_active = models.BooleanField(
        _("Active Status"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    is_verified = models.BooleanField(
        _("Verified Email"),
        default=False,
        help_text=_("Designates whether the user has verified their email.")
    )
    is_onboarded = models.BooleanField(
        _("Finished Onboarding"),
        default=False,
        help_text=_("Designates whether the user has finished onboarding.")
    )
    is_test = models.BooleanField(
        _("Test Account"),
        default=False,
        help_text=_(
            "Designates whether we should count this user in official numbers."
        )
    )
    is_staff = models.BooleanField(
        _("Staff Status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_superuser = models.BooleanField(
        _("Superuser Status"),
        default=False,
        help_text=_(
            "Designates that this user has all permissions without explicitly assigning them."
        )
    )

    # organizations
    organization = models.ManyToManyField(
        Organization,
        blank=True
    )

    # academic and test scores
    high_school_grad_year = models.PositiveIntegerField(
        _("High School Graduation Year"),
        blank=True,
        null=True,
    )
    gpa = models.DecimalField(
        _("GPA"),
        blank=True,
        decimal_places=2,
        max_digits=5,
        null=True
    )
    act_score = models.PositiveSmallIntegerField(
        _("ACT Score"),
        blank=True,
        null=True
    )
    sat_math = models.PositiveSmallIntegerField(
        _("SAT Math"),
        blank=True,
        null=True
    )
    sat_verbal = models.PositiveSmallIntegerField(
        _("SAT Verbal"),
        blank=True,
        null=True
    )

    # financial information
    efc = models.PositiveIntegerField(
        _("Expected Family Contribution"),
        blank=True,
        null=True
    )
    income = models.ForeignKey(
        Income,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = UserManager()

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def get_full_name(self):
        """ Return the first_name plus the last_name, with a space in between. """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def __str__(self):
        return self.email


################################################
### User Dependent Models
################################################
class Action(models.Model):
    user = models.ForeignKey(
        User,
        default=DEFAULT_USER_ID,
        on_delete=models.CASCADE
    )
    description = models.CharField(max_length=255)
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'action'
        verbose_name_plural = 'actions'

    def __str__(self):
        return self.description


class DeletedAccount(models.Model):
    date = models.DateField()
    accounts = models.IntegerField()

    class Meta:
        verbose_name_plural = 'deleted account'
        verbose_name_plural = 'deleted accounts'

    def __str__(self):
        return self.date


class Ethnicity(models.Model):
    ethnicity = models.CharField(max_length=255, unique=True)
    description = models.CharField(blank=True, max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'ethnicity'
        verbose_name_plural = 'ethnicities'

    def __str__(self):
        return self.ethnicity


class EthnicityUser(models.Model):
    user = models.ForeignKey(
        User,
        default=DEFAULT_USER_ID,
        on_delete=models.CASCADE
    )
    ethnicity = models.ForeignKey(
        Ethnicity,
        default=DEFAULT_ETHNICITY_ID,
        on_delete=models.CASCADE
    )
    other_value = models.CharField(blank=True, max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'ethnicity user'
        verbose_name_plural = 'ethnicity users'

    def __str__(self):
        return str(self.user)


class Pronoun(models.Model):
    pronoun = models.CharField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'pronoun'
        verbose_name_plural = 'pronouns'

    def __str__(self):
        return self.pronoun


class PronounUser(models.Model):
    user = models.ForeignKey(
        User,
        default=DEFAULT_USER_ID,
        on_delete=models.CASCADE
    )
    pronoun = models.ForeignKey(
        Pronoun,
        default=DEFAULT_PRONOUN_ID,
        on_delete=models.CASCADE
    )
    other_value = models.CharField(blank=True, max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'pronoun user'
        verbose_name_plural = 'pronoun users'

    def __str__(self):
        return str(self.user)


class Source(models.Model):
    source = models.CharField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'source'
        verbose_name_plural = 'sources'

    def __str__(self):
        return self.source


class SourceUser(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        default=DEFAULT_USER_ID,
        on_delete=models.CASCADE
    )
    source = models.ForeignKey(
        Source,
        default=DEFAULT_SOURCE_ID,
        on_delete=models.CASCADE
    )
    other_value = models.CharField(blank=True, max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'source user'
        verbose_name_plural = 'source users'

    def __str__(self):
        return str(self.user)
