import datetime

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
from organization.models import Organization


class DeletedAccount(models.Model):
    date = models.DateField()
    accounts = models.IntegerField()

    def __str__(self):
        return str(self.date)


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
    """ Custom user model that extends AbstractBaseUser and PermissionsMixin """

    DEFAULT_CHAR_TEXT = ""
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]
    CONTACT_METHOD_CHOICES = (
        ("text", "text"),
        ("email", "email")
    )

    email = models.EmailField(
        _("email address"),
        unique=True,
        error_messages={
            "unique": _("A user is already registered with this email address"),
        },
    )
    user_type = models.CharField(_("user type"), 
        default=DEFAULT_CHAR_TEXT, 
        blank=True, 
        max_length=255
    )
    first_name = models.CharField(_("first name"), max_length=255)
    last_name = models.CharField(_("last name"), max_length=255)
    preferred_name = models.CharField(_("preferred name"),
        default=DEFAULT_CHAR_TEXT, 
        max_length=255, blank=True
    )
    preferred_contact_method = models.CharField(
        _("preferred contact method"),
         blank=True,
         choices=CONTACT_METHOD_CHOICES,
         max_length=255,
    )
    phone_number = models.CharField(
        _("phone number"),
        blank=True,
        max_length=15
    )
    is_verified = models.BooleanField(default=False)
    is_onboarded = models.BooleanField(default=False)
    is_test = models.BooleanField(default=False)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    gpa = models.DecimalField(
        _("GPA"),
        blank=True,
        decimal_places=2,
        max_digits=5,
        null=True
    )
    act_score = models.PositiveSmallIntegerField(_("ACT score"), blank=True, null=True)
    sat_math = models.PositiveSmallIntegerField(_("SAT math"), blank=True, null=True)
    sat_verbal = models.PositiveSmallIntegerField(_("SAT verbal"), blank=True, null=True)
    efc = models.PositiveIntegerField(_("Expected Family Contribution"), blank=True, null=True)
    pronouns = models.CharField(_("pronoun"),
        default=DEFAULT_CHAR_TEXT, 
        max_length=255, 
        blank=True
    )
    ethnicity = ArrayField(
        models.CharField(_("ethnicity"),
            default=DEFAULT_CHAR_TEXT, 
            max_length=255, 
            blank=True
        ),
        blank=True,
        null=True,
    )
    high_school_grad_year = models.PositiveIntegerField(
        _("high school graduation year"),
        blank=True,
        null=True,
    )
    income_quintile = models.CharField(
        _("income quintile"),
        max_length=255,
        default=DEFAULT_CHAR_TEXT, 
        blank=True,
    )
    found_from = ArrayField(
        models.CharField(_("found from"), max_length=255, null=True, blank=True),
        null=True, blank=True,
    )
    organization = models.ManyToManyField(Organization)

    # automatically added
    created = models.DateTimeField(_("date joined"), auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = UserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

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

class Action(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.description