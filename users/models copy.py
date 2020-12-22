from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django_better_admin_arrayfield.models.fields import ArrayField
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from django.core.mail import send_mail
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from organizations.models import Organization
from datetime import datetime

class Pronoun(models.Model):
    #  he, she, they, other
    pronoun = models.CharField(max_length=255, null=True, blank=True)

    # automatically added
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pronoun)

class PronounUser(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        null=True, blank=True, on_delete=models.CASCADE)
    pronoun = models.ForeignKey(
        Pronoun, null=True, blank=True, on_delete=models.CASCADE)
    other_value = models.CharField(max_length=255, null=True, blank=True)

    # automatically added
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)

class Source(models.Model):
    # instagram, facebook, parent, school staff, friend, other
    source = models.CharField(max_length=255, null=True, blank=True)

    # automatically added
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.source)

class SourceUser(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        null=True, blank=True, on_delete=models.CASCADE)
    source = models.ForeignKey(
        Source, null=True, blank=True, on_delete=models.CASCADE)
    other_value = models.CharField(max_length=255, null=True, blank=True)

    # automatically added
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.source)

class Type(models.Model):
    # student, transfer, parent, staff, other
    user_type = models.CharField(max_length=255, null=True, blank=True)

    # automatically added
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user_type)

class Income(models.Model):
    # lo, m1, m2, h1, h2
    category = models.CharField(max_length=255, null=True, blank=True)
    # "$0 - 30,000", "$30,001 - $48,000", "$48,001 - $75,000", "$75,001 - $110,000", "$110,000+"
    description = models.CharField(max_length=255, null=True, blank=True)

    # automatically added
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.category)

class Ethnicity(models.Model):
    # aian, asian, black, latinx, nhpi, other, white
    ethnicity = models.CharField(max_length=255, null=True, blank=True)

    # automatically added
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.ethnicity)

class EthnicityUser(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        null=True, blank=True, on_delete=models.CASCADE)
    ethnicity = models.ForeignKey(
        Ethnicity, null=True, blank=True, on_delete=models.CASCADE)
    other_value = models.CharField(max_length=255, null=True, blank=True)

    # automatically added
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)

class UserManager(BaseUserManager):
    """
    User manager for Custom User that allows users to be created
    """

    use_in_migrations = True

    def _create_user(self, email, first_name=None, last_name=None, password=None, **extra_fields):
        if not email:
            raise ValueError("Email must be provided")
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, first_name=None, last_name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, first_name, last_name, password, **extra_fields)

    def create_superuser(self, email, first_name, last_name, password=None, **extra_fields):
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
        _("email address"), unique=True,
        error_messages={
            "unique": _("A user is already registered with this email address")})

    is_verified = models.BooleanField(default=False)
    is_onboarded = models.BooleanField(default=False)
    is_test_account = models.BooleanField(default=False)

    is_staff = models.BooleanField(
        _("staff status"), default=False,
        help_text=_(
            "Designates whether the user can log into this admin site."))

    is_active = models.BooleanField(
        _("active"), default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."))

    preferred_contact_method = models.CharField(_("preferred contact method"), 
        max_length=255, null=True, blank=True)
    first_name = models.CharField(_("first name"),
        max_length=255, null=True, blank=True)
    last_name = models.CharField(_("last name"),
        max_length=255, null=True, blank=True)
    phone_number = models.CharField(_("phone number"),
        max_length=255, null=True, blank=True)
    preferred_name = models.CharField(_("preferred name"),
        max_length=255, null=True, blank=True)
    gpa = models.DecimalField(_("GPA"),
        max_digits=5, decimal_places=2, null=True, blank=True)
    act_score = models.IntegerField(_("ACT score"),
        null=True, blank=True)
    sat_math = models.IntegerField(_("SAT math"),
        null=True, blank=True)
    sat_verbal = models.IntegerField(_("SAT verbal"),
        null=True, blank=True)
    efc = models.IntegerField(_("Expected Family Contribution"),
        null=True, blank=True)
    high_school_grad_year = models.IntegerField(_("high school graduation year"),
        null=True, blank=True)

    organization = models.ManyToManyField(Organization)
    user_type = models.ForeignKey(
        Type, null=True, blank=True, on_delete=models.CASCADE)
    income = models.ForeignKey(
        Income, null=True, blank=True, on_delete=models.CASCADE)

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

    def __str__(self):
        return str(self.email)


class DeletedAccount(models.Model):
    date = models.DateField()
    accounts = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.date)

class Action(models.Model):
    """
    Create New Action
        Action(
            user=user, 
            action='Logged In', (add description)
            timestamp=(check helpers folder for create_timestamp)
    """

    user = models.ForeignKey(
        CustomUser, null=True, blank=True, on_delete=models.CASCADE)
    description = models.CharField(
        max_length=255, default=None, null=True, blank=True)

    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.description)