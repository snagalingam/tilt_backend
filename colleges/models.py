from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django_better_admin_arrayfield.models.fields import ArrayField
from services.sendgrid_api.send_email import send_notification_email
from services.twilio_api.sms_methods import send_notification_sms

DEFAULT_COLLEGE_ID = 1
DEFAULT_COLLEGE_STATUS_ID= 1
DEFAULT_POPULARITY_SCORE = 0
DEFAULT_SCORECARD_ID = 1
DEFAULT_USER_ID = 1


################################################
### College Model
################################################
class College(models.Model):
    # google api inputted (otherwise scorecard)
    name = models.CharField(blank=True, max_length=255)
    scorecard_unit_id = models.IntegerField()

    # calculated fields
    show = models.BooleanField(default=False)
    popularity_score = models.IntegerField(default=DEFAULT_POPULARITY_SCORE)

    # google api inputted continued
    place_id = models.CharField(blank=True, max_length=255)
    address = models.CharField(blank=True, max_length=255)
    business_status = models.CharField(blank=True, max_length=255)
    description = models.TextField(blank=True, null=True)
    lat = models.DecimalField(blank=True, decimal_places=7, max_digits=10, null=True)
    lng = models.DecimalField(blank=True, decimal_places=7, max_digits=10, null=True)
    main_photo = models.TextField(blank=True, null=True)
    phone_number = models.CharField(blank=True, max_length=255)
    photos = ArrayField(
        models.TextField(blank=True, null=True),
        null=True,
        blank=True,
        default=None
    )
    types = ArrayField(
        models.CharField(blank=True, max_length=255),
        blank=True,
        null=True
    )
    url = models.TextField(blank=True)
    website = models.TextField(blank=True)

    # web search
    favicon = models.TextField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "college"
        verbose_name_plural = "colleges"

    def __str__(self):
        return self.name


################################################
### College Status
################################################
class CollegeStatus(models.Model):
    AWARD_STATUS_CHOICES = (
        ("uploaded", "uploaded"),
        ("reviewed", "reviewed"),
        ("user notified", "user notified"),
    )
    IN_STATE_TUITION_CHOICES = (
        ("yes", "yes"),
        ("no", "no"),
        ("unsure", "unsure"),
    )
    RESIDENCY_CHOICES = (
        ("oncampus", "oncampus"),
        ("offcampus with rent", "offcampus with rent"),
        ("offcampus no rent", "offcampus no rent",)
    )
    STATUS_CHOICES = (
        ("not interested", "not interested"),
        ("interested", "interested"),
        ("applied", "applied"),
        ("waitlisted", "waitlisted"),
        ("accepted", "accepted"),
        ("not accepted", "not accepted"),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        default=DEFAULT_USER_ID,
        on_delete=models.CASCADE
    )
    college = models.ForeignKey(
        College,
        default=DEFAULT_COLLEGE_ID,
        on_delete=models.PROTECT
    )
    status = models.CharField(choices=STATUS_CHOICES, max_length=255)
    award_status = models.CharField(
        blank=True,
        choices=AWARD_STATUS_CHOICES,
        max_length=255
    )
    in_state_tuition = models.CharField(
        blank=True,
        choices=IN_STATE_TUITION_CHOICES,
        max_length=255
    )
    residency = models.CharField(
        blank=True,
        choices=RESIDENCY_CHOICES,
        max_length=255
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        method = self.user.preferred_contact_method

        # send user notification about financial aid letter if award_reviewed=True
        if self.award_status == "reviewed":

            if method == "text":
                send_notification_sms(self.user.phone_number)
                self.award_status = "user notified"

            else:
                send_notification_email(self.user.email, self.user.first_name)
                self.award_status = "user notified"

        return super(CollegeStatus, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'college status'
        verbose_name_plural = 'college statuses'

    def __str__(self):
        return str(self.pk)


################################################
### Budget
################################################
class Budget(models.Model):
    college_status = models.OneToOneField(
        CollegeStatus,
        default=DEFAULT_COLLEGE_STATUS_ID,
        on_delete=models.CASCADE
    )
    family = models.IntegerField(blank=True, null=True)
    job = models.IntegerField(blank=True, null=True)
    other_scholarships = models.IntegerField(blank=True, null=True)
    savings = models.IntegerField(blank=True, null=True)
    work_study = models.IntegerField(blank=True, null=True)
    loan_plus = models.IntegerField(blank=True, null=True)
    loan_private = models.IntegerField(blank=True, null=True)
    loan_school = models.IntegerField(blank=True, null=True)
    loan_subsidized = models.IntegerField(blank=True, null=True)
    loan_unsubsidized = models.IntegerField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'budget'
        verbose_name_plural = 'budgets'

    def __str__(self):
        return str(self.pk)


################################################
### Scorecard
################################################
class Scorecard(models.Model):
    # college model
    college = models.OneToOneField(
        College,
        default=DEFAULT_COLLEGE_ID,
        on_delete=models.CASCADE
    )

    # basic info
    name = models.CharField(max_length=255)
    unit_id = models.IntegerField(null=True)
    show = models.BooleanField(default=False)
    ope_id = models.CharField(max_length=20)
    ope6_id = models.CharField(max_length=20)

    # location
    city = models.CharField(max_length=255)
    latitude = models.DecimalField(decimal_places=6, max_digits=9, null=True)
    longitude = models.DecimalField(decimal_places=6, max_digits=9, null=True)
    state = models.CharField(max_length=255)
    state_fips = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)

    # general information
    alias = models.CharField(blank=True, max_length=255)
    accreditor = models.CharField(max_length=255)
    branches = models.IntegerField(blank=True, null=True)
    carnegie_basic = models.CharField(blank=True, max_length=255)
    carnegie_size_setting = models.CharField(blank=True, max_length=255)
    carnegie_size_setting_size = models.CharField(blank=True, max_length=255)
    carnegie_size_setting_residential = models.CharField(blank=True, max_length=255)
    carnegie_undergrad = models.CharField(blank=True, max_length=255)
    highest_degree_awarded = models.CharField(blank=True, max_length=255)
    institutional_level = models.CharField(max_length=255, blank=True)
    locale = models.CharField(blank=True, max_length=255)
    locale_updated = models.CharField(blank=True, max_length=255)
    main_campus = models.BooleanField(default=False)
    online_only = models.BooleanField(default=False)
    operating = models.BooleanField(default=False)
    ownership = models.CharField(max_length=255)
    predominant_degree_awarded = models.CharField(blank=True, max_length=255)
    predominant_degree_awarded_recoded = models.CharField(blank=True, max_length=255)
    price_calculator_url = models.CharField(blank=True, max_length=255)
    region = models.CharField(blank=True, max_length=255)
    school_url = models.CharField(blank=True, max_length=255)
    under_investigation = models.BooleanField(blank=True, null=True, default=False)

    # institution types
    minority_serving_aanipi = models.BooleanField(default=False)
    minority_serving_annh = models.BooleanField(default=False)
    minority_serving_hispanic = models.BooleanField(default=False)
    minority_serving_historically_black  = models.BooleanField(default=False)
    minority_serving_nant = models.BooleanField(default=False)
    minority_serving_predominantly_black  = models.BooleanField(default=False)
    minority_serving_tribal = models.BooleanField(default=False)
    men_only = models.BooleanField(default=False)
    women_only = models.BooleanField(default=False)
    religious_affiliation = models.CharField(blank=True, max_length=255)

    # admissions
    admissions_rate = models.DecimalField(blank=True, decimal_places=4, max_digits=7, null=True)
    open_admissions = models.BooleanField(default=False)
    act_cumulative_25th_percentile = models.PositiveIntegerField(blank=True, null=True)
    act_cumulative_75th_percentile = models.PositiveIntegerField(blank=True, null=True)
    act_cumulative_midpoint = models.PositiveIntegerField(blank=True, null=True)
    act_english_25th_percentile = models.PositiveIntegerField(blank=True, null=True)
    act_english_75th_percentile = models.PositiveIntegerField(blank=True, null=True)
    act_english_midpoint = models.PositiveIntegerField(blank=True, null=True)
    act_math_25th_percentile = models.PositiveIntegerField(blank=True, null=True)
    act_math_75th_percentile = models.PositiveIntegerField(blank=True, null=True)
    act_math_midpoint = models.PositiveIntegerField(blank=True, null=True)
    act_writing_25th_percentile = models.PositiveIntegerField(blank=True, null=True)
    act_writing_75th_percentile = models.PositiveIntegerField(blank=True, null=True)
    act_writing_midpoint = models.PositiveIntegerField(blank=True, null=True)
    sat_average = models.PositiveIntegerField(blank=True, null=True)
    sat_math_25th_percentile = models.PositiveIntegerField(blank=True, null=True)
    sat_math_75th_percentile = models.PositiveIntegerField(blank=True, null=True)
    sat_math_midpoint = models.PositiveIntegerField(blank=True, null=True)
    sat_reading_25th_percentile = models.PositiveIntegerField(blank=True, null=True)
    sat_reading_75th_percentile = models.PositiveIntegerField(blank=True, null=True)
    sat_reading_midpoint = models.PositiveIntegerField(blank=True, null=True)
    sat_writing_25th_percentile = models.PositiveIntegerField(blank=True, null=True)
    sat_writing_75th_percentile = models.PositiveIntegerField(blank=True, null=True)
    sat_writing_midpoint = models.PositiveIntegerField(blank=True, null=True)

    # undergraduate students description
    undergraduate_students = models.PositiveIntegerField(blank=True, null=True)
    undergraduate_students_2ormore = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    undergraduate_students_aian = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    undergraduate_students_asian = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    undergraduate_students_black = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    undergraduate_students_hispanic = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    undergraduate_students_nhpi = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    undergraduate_students_nra = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    undergraduate_students_unknown = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    undergraduate_students_white = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    undergraduate_students_parttime = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    undergraduate_students_men = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    undergraduate_students_women = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    age_entry = models.PositiveIntegerField(blank=True, null=True)
    first_generation = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    share_25_older = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    veteran = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)

    # cost and net price fields
    avg_net_price = models.IntegerField(blank=True, null=True)
    avg_net_price_lo = models.IntegerField(blank=True, null=True)
    avg_net_price_m1 = models.IntegerField(blank=True, null=True)
    avg_net_price_m2 = models.IntegerField(blank=True, null=True)
    avg_net_price_h1 = models.IntegerField(blank=True, null=True)
    avg_net_price_h2 = models.IntegerField(blank=True, null=True)
    cost_of_attendance = models.IntegerField(blank=True, null=True)
    tuition_in_state = models.IntegerField(blank=True, null=True)
    tuition_out_of_state = models.IntegerField(blank=True, null=True)
    tuition_program_year = models.IntegerField(blank=True, null=True)

    # loan, grant, and earnings fields
    default_rate_2yr = models.DecimalField(blank=True, decimal_places=3, max_digits=4, null=True)
    default_rate_2yr_num_students = models.PositiveIntegerField(blank=True, null=True)
    default_rate_3yr = models.DecimalField(blank=True, decimal_places=3, max_digits=4, null=True)
    default_rate_3yr_num_students = models.PositiveIntegerField(blank=True, null=True)
    federal_loan_rate = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    median_debt = models.PositiveIntegerField(blank=True, null=True)
    median_debt_num_students = models.PositiveIntegerField(blank=True, null=True)
    median_debt_completers = models.PositiveIntegerField(blank=True, null=True)
    median_debt_completers_num_students = models.PositiveIntegerField(blank=True, null=True)
    median_debt_noncompleters = models.PositiveIntegerField(blank=True, null=True)
    median_debt_noncompleters_num_students = models.PositiveIntegerField(blank=True, null=True)
    monthly_loan_payments = models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)
    plus_loan_median_debt = models.PositiveIntegerField(blank=True, null=True)
    plus_loan_median_debt_num_students = models.PositiveIntegerField(blank=True, null=True)
    plus_loan_pct_lower = models.PositiveIntegerField(blank=True, null=True)
    plus_loan_pct_upper = models.PositiveIntegerField(blank=True, null=True)
    pell_grant_rate = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    students_with_any_loan  = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    students_with_pell_grant = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)

    # earnings
    not_working_not_enrolled_3yr_num_students = models.PositiveIntegerField(blank=True, null=True)
    working_not_enrolled_3yr_num_students = models.PositiveIntegerField(blank=True, null=True)
    over_poverty_line_3yr_num_students = models.PositiveIntegerField(blank=True, null=True)

    # graduation rate fields
    graduation_rate_100 = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    graduation_rate_100_num_students = models.PositiveIntegerField(blank=True, null=True)
    graduation_rate_150 = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    graduation_rate_150_num_students = models.PositiveIntegerField(blank=True, null=True)
    graduation_rate_150_2ormore = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    graduation_rate_150_2ormore_num_students = models.PositiveIntegerField(blank=True, null=True)
    graduation_rate_150_aian = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    graduation_rate_150_aian_num_students = models.PositiveIntegerField(blank=True, null=True)
    graduation_rate_150_asian = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    graduation_rate_150_asian_num_students = models.PositiveIntegerField(blank=True, null=True)
    graduation_rate_150_black = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    graduation_rate_150_black_num_students = models.PositiveIntegerField(blank=True, null=True)
    graduation_rate_150_hispanic = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    graduation_rate_150_hispanic_num_students = models.PositiveIntegerField(blank=True, null=True)
    graduation_rate_150_nhpi = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    graduation_rate_150_nhpi_num_students = models.PositiveIntegerField(blank=True, null=True)
    graduation_rate_150_nra = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    graduation_rate_150_nra_num_students = models.PositiveIntegerField(blank=True, null=True)
    graduation_rate_150_unknown = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    graduation_rate_150_unknown_num_students = models.PositiveIntegerField(blank=True, null=True)
    graduation_rate_150_white = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    graduation_rate_150_white_num_students = models.PositiveIntegerField(blank=True, null=True)
    graduation_rate_200 = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    graduation_rate_200_num_students = models.PositiveIntegerField(blank=True, null=True)

    # first time full time
    first_time_full_time = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    first_time_full_time_federal_loan_rate = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    first_time_full_time_pell_grant_rate = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    first_time_full_time_num_students = models.PositiveIntegerField(blank=True, null=True)

    # retention rate
    retention_rate_full_time = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    retention_rate_part_time = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)

    # program percentages
    program_percentage_agriculture = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    program_percentage_architecture = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    program_percentage_biological = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    program_percentage_business_marketing = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    program_percentage_communication = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    program_percentage_communications_technology = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    program_percentage_computer = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    program_percentage_construction = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    program_percentage_education = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    program_percentage_engineering = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    program_percentage_engineering_technology = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    program_percentage_english = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    program_percentage_ethnic_cultural_gender = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    program_percentage_family_consumer_science = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    program_percentage_health = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    program_percentage_history = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    program_percentage_humanities = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    program_percentage_language = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    program_percentage_legal = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    program_percentage_library = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    program_percentage_mathematics = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    program_percentage_mechanic_repair_technology = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    program_percentage_military = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    program_percentage_multidiscipline = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    program_percentage_parks_recreation_fitness = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    program_percentage_personal_culinary = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    program_percentage_philosophy_religious = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    program_percentage_physical_science = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    program_percentage_precision_production = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    program_percentage_psychology = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    program_percentage_public_administration_social_service = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    program_percentage_resources = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    program_percentage_science_technology = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    program_percentage_security_law_enforcement = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    program_percentage_social_science = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    program_percentage_theology_religious_vocation = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    program_percentage_transportation = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)
    program_percentage_visual_performing = models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)

    # automatically added
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = 'scorecard'
        verbose_name_plural = 'scorecards'

    def __str__(self):
        return self.name


################################################
### Field of Study
################################################
class FieldOfStudy(models.Model):
    college = models.ForeignKey(
        College,
        on_delete=models.CASCADE,
        default=DEFAULT_COLLEGE_ID
    )
    scorecard = models.ForeignKey(
        Scorecard,
        on_delete=models.CASCADE,
        default=DEFAULT_SCORECARD_ID,
    )
    show = models.BooleanField(default=False)
    cip_code = models.CharField(blank=True, max_length=255)
    cip_title = models.CharField(blank=True, max_length=255)
    credential_level = models.CharField(blank=True, max_length=255)
    credential_title = models.CharField(blank=True, max_length=255)

    # debt
    debt_num_students = models.PositiveIntegerField(blank=True, null=True)
    debt_mean = models.PositiveIntegerField(blank=True, null=True)
    debt_median = models.PositiveIntegerField(blank=True, null=True)
    debt_monthly_payment = models.PositiveIntegerField(blank=True, null=True)
    plus_debt_num_students = models.PositiveIntegerField(blank=True, null=True)
    plus_debt_mean = models.PositiveIntegerField(blank=True, null=True)
    plus_debt_median = models.PositiveIntegerField(blank=True, null=True)
    plus_debt_monthly_payment = models.PositiveIntegerField(blank=True, null=True)

    # earnings
    earnings_1yr_median_earnings = models.PositiveIntegerField(blank=True, null=True)
    earnings_1yr_not_working_not_enrolled_num_students = models.PositiveIntegerField(blank=True, null=True)
    earnings_1yr_over_poverty_line_num_students = models.PositiveIntegerField(blank=True, null=True)
    earnings_1yr_working_not_enrolled_num_students = models.PositiveIntegerField(blank=True, null=True)
    earnings_2yr_median_earnings = models.PositiveIntegerField(blank=True, null=True)
    earnings_2yr_not_working_not_enrolled_num_students = models.PositiveIntegerField(blank=True, null=True)
    earnings_2yr_over_poverty_line_num_students = models.PositiveIntegerField(blank=True, null=True)
    earnings_2yr_working_not_enrolled_num_students = models.PositiveIntegerField(blank=True, null=True)

    # ipeds awards
    ipeds_awards1_num_students = models.IntegerField(blank=True, null=True)
    ipeds_awards2_num_students = models.IntegerField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'field of study'
        verbose_name_plural = 'fields of studies'

    def __str__(self):
        return self.cip_title
