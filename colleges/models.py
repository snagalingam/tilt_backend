from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django_better_admin_arrayfield.models.fields import ArrayField


class College(models.Model):

    # popularity_score
    popularity_score = models.IntegerField(default=0, blank=True, null=True)

    # college scorecard info
    unit_id = models.CharField(max_length=255, blank=True, null=True)
    ope_id = models.CharField(max_length=255, blank=True, null=True)

    # google api inputted
    place_id = models.CharField(max_length=255, blank=True, null=True)
    business_status = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)
    url = models.TextField(null=True, blank=True)
    website = models.TextField(null=True, blank=True)
    favicon = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    main_photo = models.TextField(null=True, blank=True)
    photos = ArrayField(
        models.TextField(null=True, blank=True),
        null=True, blank=True, default=None
    )
    types = ArrayField(
        models.CharField(max_length=255, null=True, blank=True),
        null=True, blank=True, default=None
    )

    # automatically added
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.name)


class Scorecard(models.Model):
    # college model
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    # school info fields
    unit_id = models.IntegerField(blank=True, null=True)
    ope_id = models.CharField(max_length=255, blank=True, null=True)
    ope6_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    zipcode = models.CharField(max_length=255, blank=True, null=True)
    accreditor = models.CharField(max_length=255, blank=True, null=True)
    school_url = models.CharField(max_length=255, blank=True, null=True)
    price_calculator_url = models.CharField(
        max_length=255, blank=True, null=True)
    predominant_degree_awarded_recoded = models.CharField(
        max_length=255, blank=True, null=True)
    under_investigation = models.BooleanField(blank=True, null=True)
    main_campus = models.BooleanField(blank=True, null=True)
    branches = models.IntegerField(blank=True, null=True)
    predominant_degree_awarded = models.CharField(
        max_length=255, blank=True, null=True)
    highest_degree_awarded = models.CharField(max_length=255, blank=True, null=True)
    ownership = models.CharField(max_length=255, blank=True, null=True)
    state_fips = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    locale = models.CharField(max_length=255, blank=True, null=True)
    degree_urbanization = models.CharField(
        max_length=255, blank=True, null=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    carnegie_basic = models.CharField(max_length=255, blank=True, null=True)
    carnegie_undergrad = models.CharField(
        max_length=255, blank=True, null=True)
    carnegie_size_setting = models.CharField(
        max_length=255, blank=True, null=True)

    # diversity fields
    minority_serving_historically_black = models.BooleanField(
        blank=True, null=True)
    minority_serving_predominantly_black = models.BooleanField(
        blank=True, null=True)
    minority_serving_annh = models.BooleanField(
        blank=True, null=True)
    minority_serving_tribal = models.BooleanField(blank=True, null=True)
    minority_serving_aanipi = models.BooleanField(blank=True, null=True)
    minority_serving_hispanic = models.BooleanField(blank=True, null=True)
    minority_serving_nant = models.BooleanField(blank=True, null=True)
    men_only = models.BooleanField(blank=True, null=True)
    women_only = models.BooleanField(blank=True, null=True)
    religious_affiliation = models.CharField(
        max_length=255, blank=True, null=True)

    # admission fields
    admissions_rate = models.FloatField(null=True, blank=True)
    sat_reading_25th_percentile = models.FloatField(null=True, blank=True)
    sat_reading_75th_percentile = models.FloatField(null=True, blank=True)
    sat_math_25th_percentile = models.FloatField(null=True, blank=True)
    sat_math_75th_percentile = models.FloatField(null=True, blank=True)
    sat_writing_25th_percentile = models.FloatField(null=True, blank=True)
    sat_writing_75th_percentile = models.FloatField(null=True, blank=True)
    sat_reading_midpoint = models.FloatField(null=True, blank=True)
    sat_math_midpoint = models.FloatField(null=True, blank=True)
    sat_writing_midpoint = models.FloatField(null=True, blank=True)
    act_cumulative_25th_percentile = models.FloatField(null=True, blank=True)
    act_cumulative_75th_percentile = models.FloatField(null=True, blank=True)
    act_english_25th_percentile = models.FloatField(null=True, blank=True)
    act_english_75th_percentile = models.FloatField(null=True, blank=True)
    act_math_25th_percentile = models.FloatField(null=True, blank=True)
    act_math_75th_percentile = models.FloatField(null=True, blank=True)
    act_writing_25th_percentile = models.FloatField(null=True, blank=True)
    act_writing_75th_percentile = models.FloatField(null=True, blank=True)
    act_cumulative_midpoint = models.FloatField(null=True, blank=True)
    act_english_midpoint = models.FloatField(null=True, blank=True)
    act_math_midpoint = models.FloatField(null=True, blank=True)
    act_writing_midpoint = models.FloatField(null=True, blank=True)
    sat_average = models.FloatField(null=True, blank=True)
    online_only = models.BooleanField(blank=True, null=True)

    # undergraduate fields
    undergraduate_students = models.FloatField(null=True, blank=True)
    undergraduate_students_white = models.FloatField(null=True, blank=True)
    undergraduate_students_black = models.FloatField(null=True, blank=True)
    undergraduate_students_hispanic = models.FloatField(null=True, blank=True)
    undergraduate_students_asian = models.FloatField(null=True, blank=True)
    undergraduate_students_aian = models.FloatField(null=True, blank=True)
    undergraduate_students_nhpi = models.FloatField(null=True, blank=True)
    undergraduate_students_2ormore = models.FloatField(null=True, blank=True)
    undergraduate_students_nra = models.FloatField(null=True, blank=True)
    undergraduate_students_unknown = models.FloatField(null=True, blank=True)
    undergraduate_students_parttime = models.FloatField(null=True, blank=True)
    operating = models.BooleanField(blank=True, null=True)

    # net pricing fields
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
    pell_grant_rate = models.FloatField(null=True, blank=True)

    # loan fields
    federal_loan_rate = models.FloatField(null=True, blank=True)
    share_25_older = models.FloatField(null=True, blank=True)
    default_rate_2yr = models.FloatField(null=True, blank=True)
    default_rate_3yr = models.FloatField(null=True, blank=True)
    median_debt = models.FloatField(null=True, blank=True)
    median_debt_completers = models.FloatField(null=True, blank=True)
    median_debt_noncompleters = models.FloatField(null=True, blank=True)
    median_debt_num_students = models.IntegerField(blank=True, null=True)
    median_debt_completers_num_students = models.IntegerField(blank=True, null=True)
    median_debt_noncompleters_num_students = models.IntegerField(
        blank=True, null=True)
    monthly_loan_payments = models.FloatField(null=True, blank=True)
    students_with_any_loan = models.FloatField(null=True, blank=True)
    students_with_pell_grant = models.FloatField(null=True, blank=True)
    age_entry = models.IntegerField(blank=True, null=True)
    veteran = models.FloatField(null=True, blank=True)
    first_generation = models.FloatField(null=True, blank=True)
    alias = models.TextField(blank=True, null=True)


    # graduation rate fields
    graduation_rate_100 = models.FloatField(null=True, blank=True)
    graduation_rate_100_num_students = models.IntegerField(
        blank=True, null=True)
    institutional_level = models.CharField(
        max_length=255, blank=True, null=True)

    undergraduate_students_men = models.FloatField(null=True, blank=True)
    undergraduate_students_women = models.FloatField(null=True, blank=True)
    default_rate_2yr_num_students = models.IntegerField(blank=True, null=True)
    default_rate_3yr_num_students = models.IntegerField(blank=True, null=True)
    open_admissions = models.BooleanField(blank=True, null=True)
    graduation_rate_150 = models.FloatField(null=True, blank=True)
    first_time_full_time = models.FloatField(null=True, blank=True)
    graduation_rate_150_white = models.FloatField(null=True, blank=True)
    graduation_rate_150_black = models.FloatField(null=True, blank=True)
    graduation_rate_150_hispanic = models.FloatField(null=True, blank=True)
    graduation_rate_150_asian = models.FloatField(null=True, blank=True)
    graduation_rate_150_aian = models.FloatField(null=True, blank=True)
    graduation_rate_150_nhpi = models.FloatField(null=True, blank=True)
    graduate_rate_150_2ormore = models.FloatField(null=True, blank=True)
    graduate_rate_150_nra = models.FloatField(null=True, blank=True)
    graduate_rate_150_unknown = models.FloatField(null=True, blank=True)
    graduation_rate_150_white_num_students = models.IntegerField(
        blank=True, null=True)
    graduation_rate_150_black_num_students = models.IntegerField(blank=True, null=True)
    graduation_rate_150_hispanic_num_students = models.IntegerField(blank=True, null=True)
    graduation_rate_150_asian_num_students = models.IntegerField(blank=True, null=True)
    graduation_rate_150_aian_num_students = models.IntegerField(
        blank=True, null=True)
    graduation_rate_150_nhpi_num_students = models.IntegerField(blank=True, null=True)
    graduate_rate_150_2ormore_num_students = models.IntegerField(
        blank=True, null=True)
    graduate_rate_150_nra_num_students = models.IntegerField(blank=True, null=True)
    graduate_rate_150_unknown_num_students = models.IntegerField(
        blank=True, null=True)
    first_time_full_time_pell_grant_rate = models.FloatField(
        null=True, blank=True)
    first_time_full_time_federal_loan_rate = models.FloatField(
        null=True, blank=True)
    first_time_full_time_num_students = models.FloatField(
        null=True, blank=True)
    graduation_rate_200 = models.FloatField(null=True, blank=True)
    retention_rate_full_time = models.FloatField(null=True, blank=True)
    retention_rate_part_time = models.FloatField(null=True, blank=True)

    # automatically added
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.name)