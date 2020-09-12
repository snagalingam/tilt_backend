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
from organizations.models import Organization


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

    is_onboarded = models.BooleanField(default=False)

    first_name = models.CharField(
        _("first name"), max_length=50, null=True, blank=True)

    last_name = models.CharField(
        _("last name"), max_length=150, null=True, blank=True)

    preferred_name = models.CharField(
        _("preferred name"), max_length=120, null=True, blank=True)

    gpa = models.DecimalField(
        _("GPA"), max_digits=4, decimal_places=2, null=True, blank=True)

    act_score = models.PositiveSmallIntegerField(
        _("ACT score"), null=True, blank=True)

    sat_score = models.PositiveSmallIntegerField(
        _("SAT score"), null=True, blank=True)

    efc = models.IntegerField(
        _("Expected Family Contribution"), null=True, blank=True)

    pronouns = models.CharField(
        _("pronoun"), max_length=10, default=None, null=True)

    ethnicity = ArrayField(
        models.CharField(
            _("ethnicity"), max_length=25, null=True))


    user_type = models.CharField(
        _("user type"), max_length=10, null=True, default=None)

    organization = models.ManyToManyField(Organization)

    high_school_grad_year = models.IntegerField(
        _("high school graduation year"), null=True, blank=True
    )

    income_quintile = models.CharField(
        _("income quintile"), max_length=4, null=True, default=None)

    found_from = ArrayField(
        models.CharField(
            _("found from"), max_length=25, null=True))

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
