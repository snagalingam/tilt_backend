from colleges.models import College
from django.conf import settings
from django.db import models
from django.utils import timezone
from django_better_admin_arrayfield.models.fields import ArrayField


DEFAULT_EDUCATION_CATEGORY_ID = 1
DEFAULT_EDUCATION_DETAIL_ID = 1
DEFAULT_FIELD_CATEGORY_ID = 1
DEFAULT_FIELD_DETAIL_ID = 1
DEFAULT_LOCATION_DETAIL_ID = 1
DEFAULT_PROVIDER_ID = 1
DEFAULT_SCHOLARSHIP_ID = 1
DEFAULT_STATE_ID = 1
DEFAULT_USER_ID = 1


################################################
### Foreign Key Fields in Provider
################################################
class State(models.Model):
    name = models.CharField(max_length=50, unique=True)
    abbreviation = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'state'
        verbose_name_plural = 'states'

    def __str__(self):
        return self.name


################################################
### Provider
################################################
class Provider(models.Model):
    organization = models.CharField(max_length=255, unique=True)
    addressee = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    phone_number_ext = models.CharField(max_length=10, blank=True)
    street = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.ForeignKey(State, null=True, blank=True, on_delete=models.CASCADE)
    zipcode = models.CharField(max_length=255, blank=True)

    # automatically added
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'provider'
        verbose_name_plural = 'providers'

    def __str__(self):
        return str(self.organization)


################################################
### Foreign Key Fields in Scholarship
################################################
class Association(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "association"
        verbose_name_plural = "associations"

    def __str__(self):
        return self.name


class Citizenship(models.Model):
    category = models.CharField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "citizenship"
        verbose_name_plural = "citizenships"

    def __str__(self):
        return self.category


class Degree(models.Model):
    category = models.CharField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "degree"
        verbose_name_plural = "degrees"

    def __str__(self):
        return self.category


class Disability(models.Model):
    category = models.CharField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "disability"
        verbose_name_plural = "disabilities"

    def __str__(self):
        return self.category


class Gender(models.Model):
    category = models.CharField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "gender"
        verbose_name_plural = "genders"

    def __str__(self):
        return self.category

class Heritage(models.Model):
    category = models.CharField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "heritage"
        verbose_name_plural = "heritages"

    def __str__(self):
        return self.category

class Interest(models.Model):
    category = models.CharField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "interest"
        verbose_name_plural = "interests"

    def __str__(self):
        return self.category


class Military(models.Model):
    category = models.CharField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "military"
        verbose_name_plural = "militaries"

    def __str__(self):
        return self.category


################################################
### Scholarship Model
################################################
class Scholarship(models.Model):
    # scholarship details
    name = models.CharField(max_length=255, unique=True)
    provider = models.ForeignKey(
        Provider,
        default=DEFAULT_PROVIDER_ID,
        on_delete=models.CASCADE
    )
    deadline = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)
    max_amount = models.PositiveIntegerField(blank=True, null=True)
    number_awards = models.PositiveIntegerField(blank=True, null=True)
    renewable = models.BooleanField(default=False)
    website = models.TextField(blank=True)

    # requirements
    financial_need = models.BooleanField(default=False)
    first_generation = models.BooleanField(default=False)
    min_act = models.IntegerField(blank=True, null=True)
    min_sat = models.IntegerField(blank=True, null=True)
    min_gpa = models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)
    max_gpa = models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)
    writing = models.BooleanField(default=False)
    # relationships to other models
    association = models.ManyToManyField(Association, blank=True)
    citizenship = models.ManyToManyField(Citizenship, blank=True)
    college = models.ManyToManyField(College, blank=True)
    degree = models.ManyToManyField(Degree, blank=True)
    disability = models.ManyToManyField(Disability, blank=True)
    gender = models.ManyToManyField(Gender, blank=True)
    heritage = models.ManyToManyField(Heritage, blank=True)
    interest = models.ManyToManyField(Interest, blank=True)
    military = models.ManyToManyField(Military, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'scholarship'
        verbose_name_plural = 'scholarships'

    def __str__(self):
        return self.name


################################################
### Scholarship Dependent Models
################################################
class EducationCategory(models.Model):
    category = models.CharField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'education level'
        verbose_name_plural = 'education levels'

    def __str__(self):
        return self.category


class EducationDetail(models.Model):
    description = models.CharField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'education detail'
        verbose_name_plural = 'education details'

    def __str__(self):
        return self.description


class EducationScholarship(models.Model):
    scholarship = models.ForeignKey(
        Scholarship,
        default=DEFAULT_SCHOLARSHIP_ID,
        on_delete=models.CASCADE
    )
    education_category = models.ForeignKey(
        EducationCategory,
        default=DEFAULT_EDUCATION_CATEGORY_ID,
        on_delete=models.CASCADE
    )
    education_detail = models.ForeignKey(
        EducationDetail,
        default=DEFAULT_EDUCATION_DETAIL_ID,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'education scholarship'
        verbose_name_plural = 'education scholarships'

    def __str__(self):
        return str(self.scholarship)


class FieldCategory(models.Model):
    category = models.CharField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'field category'
        verbose_name_plural = 'field categories'

    def __str__(self):
        return self.category


class FieldDetail(models.Model):
    description = models.CharField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'field detail'
        verbose_name_plural = 'field details'

    def __str__(self):
        return self.description


class FieldScholarship(models.Model):
    scholarship = models.ForeignKey(
        Scholarship,
        default=DEFAULT_SCHOLARSHIP_ID,
        on_delete=models.CASCADE
    )
    field_category = models.ForeignKey(
        FieldCategory,
        default=DEFAULT_FIELD_CATEGORY_ID,
        on_delete=models.CASCADE
    )
    field_detail = models.ForeignKey(
        FieldDetail,
        default=DEFAULT_FIELD_DETAIL_ID,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'field scholarship'
        verbose_name_plural = 'field scholarships'

    def __str__(self):
        return str(self.scholarship)


class LocationDetail(models.Model):
    description = models.CharField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'location detail'
        verbose_name_plural = 'location details'

    def __str__(self):
        return self.description


class LocationScholarship(models.Model):
    scholarship = models.ForeignKey(
        Scholarship,
        default=DEFAULT_SCHOLARSHIP_ID,
        on_delete=models.CASCADE
    )
    state = models.ForeignKey(
        State,
        default=DEFAULT_STATE_ID,
        on_delete=models.CASCADE
    )
    location_detail = models.ForeignKey(
        LocationDetail,
        default=DEFAULT_LOCATION_DETAIL_ID,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'location scholarship'
        verbose_name_plural = 'location scholarships'

    def __str__(self):
        return str(self.scholarship)


class ScholarshipStatus(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        default=DEFAULT_USER_ID,
        on_delete=models.CASCADE
    )
    scholarship = models.ForeignKey(
        Scholarship,
        default=DEFAULT_SCHOLARSHIP_ID,
        on_delete=models.CASCADE
    )
    status = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'scholarhip status'
        verbose_name_plural = 'scholarship statuses'

    def __str__(self):
        return str(self.user)
