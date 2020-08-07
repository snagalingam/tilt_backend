from django.contrib.auth.base_user import (
    AbstractBaseUser,
    BaseUserManager,
)
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from enum import Enum
from django.core.mail import send_mail
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """
    User manager for Custom User that allows users to be created
    """

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


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model that extends AbstractBaseUser and PermissionsMixin
    """

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"

    REQUIRED_FIELDS = ["first_name", "last_name"]

    email = models.EmailField(
        _("email address"),
        unique=True,
        error_messages={
            "unique": _("A user is already registered with this email address"),
        },
    )

    is_verified = models.BooleanField(default=False)
    first_name = models.CharField(
        _("first name"), max_length=50, null=True, blank=True)
    last_name = models.CharField(
        _("last name"), max_length=150, null=True, blank=True)
    preferred_name = models.CharField(
        _("preferred name"), max_length=120, null=True, blank=True
    )
    gpa = models.DecimalField(
        _("GPA"), max_digits=4, decimal_places=2, null=True, blank=True
    )
    act_score = models.PositiveSmallIntegerField(
        _("ACT score"), null=True, blank=True)
    sat_score = models.PositiveSmallIntegerField(
        _("SAT score"), null=True, blank=True)
    efc = models.IntegerField(
        _("Expected Family Contribution"), null=True, blank=True)
    terms_and_conditions = models.BooleanField(default=False)

    # Pronouns Field
    PRONOUN_CHOICES = [
        (None, ""),
        ("he", "He/His"),
        ("she", "She/Hers"),
        ("they", "They/their"),
        ("other", "Other"),
    ]

    pronouns = models.CharField(
        _("pronoun"), max_length=10, choices=PRONOUN_CHOICES, default=None, null=True
    )

    # Ethnicty Field
    ETHNICITY_CHOICES = [
        (None, ""),
        ("american indian and alaska native", "American Indian/Alaska Native"),
        ("asian", "Asian"),
        ("black and african", "Black/African"),
        ("hispanic and latinx", "Hispanic/Latinx"),
        ("native hawaiian and pacific islander",
         "Native Hawaiian/Pacific Islander"),
        ("white", "White"),
        ("other", "Other"),
    ]
    ethnicity = models.CharField(
        _("ethinicity"),
        max_length=40,
        choices=ETHNICITY_CHOICES,
        default=None,
        null=True,
    )

    # UI Value                 | Database Value
    # -----------------------------------------
    # K-12 Student             | Student
    # Transfer Student         | Transfer
    # Parent                   | Parent
    # School or District Staff | Staff
    # Other                    | Other

    # UserType Field
    USER_TYPE_CHOICES = [
        ("student", "Student"),
        ("transfer", "Transfer"),
        ("parent", "Parent"),
        ("staff", "Staff"),
        ("other", "Other"),
    ]

    user_type = models.CharField(
        _("user type"), max_length=10, choices=USER_TYPE_CHOICES
    )

    high_school_grad_year = models.CharField(
        _("high school graduation year"),
        max_length=4, null=True, blank=True
    )

    # UI Value                 | Database Value
    # -----------------------------------------
    # $0 - $30,000             | lo
    # $30,001 - $48,000        | m1
    # $48,001 - $75,000        | m2
    # $75,001 - $110,000       | h1
    # $110,001+                | h2

    # income_quintile Field
    INCOME_QUINTILE_CHOICES = [
        ("lo", "$0 - $30,000"),
        ("m1", "$30,001 - $48,000"),
        ("m2", "$48,001 - $75,000"),
        ("h1", "$75,001 - $110,000"),
        ("h2", "$110,001+"),
    ]

    income_quintile = models.CharField(
        _("income quintile"), max_length=2, choices=INCOME_QUINTILE_CHOICES, null=True, blank=True
    )

    # UI Value                 | Database Value
    # -----------------------------------------
    # Instagram                | instagram
    # Facebook                 | facebook
    # Parent                   | parent
    # School or District Staff | school or district staff
    # Friend                   | friend
    # Other                    | (user inputs value)

    # income_quintile Field
    FOUND_FROM_CHOICES = [
        ("instagram", "Instagram"),
        ("facebook", "Facebook"),
        ("parent", "Parent"),
        ("school or district staff", "School or District Staff"),
        ("friend", "Friend"),
        ("other", "Other")
    ]

    found_from = ArrayField(
        models.CharField(
            _("found from"), max_length=25, choices=FOUND_FROM_CHOICES),
        default=list
    )

    found_from_other_value = models.CharField(
        max_length=75, null=True, blank=True
    )

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_(
            "Designates whether the user can log into this admin site."),
    )

    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = UserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)
