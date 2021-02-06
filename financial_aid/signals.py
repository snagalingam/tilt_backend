from colleges.models import CollegeStatus, Ipeds
from financial_aid.models import AidCategory, AidFinalData, AidRawData, DocumentResult
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver


@receiver(post_save, sender=AidRawData, dispatch_uid='calculate_aid_summary')
def calculate_aid_summary(sender, instance, **kwargs):

    # set total values to 0
    total_aid = 0
    total_cost = 0

    # other models
    college_status = instance.college_status
    user = college_status.user

    # aid categories
    fees_category = AidCategory.objects.get(name="fees")
    grant_categories = AidCategory.objects.filter(primary="grant")
    loan_categories = AidCategory.objects.filter(primary="loan")
    meals_category = AidCategory.objects.get(name="meals")
    personal_expenses_category = AidCategory.objects.get(name="standard personal expenses")
    room_category = AidCategory.objects.get(name="room")
    room_board_category = AidCategory.objects.get(name="room & board")
    tuition_category = AidCategory.objects.get(name="tuition")
    tuition_fees_category = AidCategory.objects.get(name="tuition & fees")
    work_study_category = AidCategory.objects.get(name="work study")

    # get ipeds object for costs
    ipeds = Ipeds.objects.get(college=college_status.college)

    ################ tuition and fees
    try:
        tuition = AidRawData.objects.get(college_status=college_status, aid_category=tuition_category)
    except:
        tuition = None

    try:
        fees = AidRawData.objects.get(college_status=college_status, aid_category=fees_category)
    except:
        fees = None

    # use raw data if that exists
    if tuition is not None:
        tuition_fees_amount = tuition.amount

        if fees is not None:
            tuition_fees_amount += fees.amount

    # otherwise, pull the data from ipeds
    else:
        if college_status.in_state_tuition == "yes":
            tuition_amount = ipeds.tuition_in_state
            fees_amount = ipeds.fees_in_state

        else:
            tuition_amount = ipeds.tuition_out_of_state
            fees_amount = ipeds.fees_out_of_state

        tuition_fees_amount = tuition_amount + fees_amount

    # update it if it already exists
    try:
        final_tuition_fees = AidFinalData.objects.get(
            aid_category=tuition_fees_category,
            college_status=college_status,
        )

        if final_tuition_fees.amount != tuition_fees_amount:
            final_tuition_fees.update(amount=tuition_fees_amount)

    # create a new one if it doesn't
    except:
        AidFinalData.objects.create(
            aid_category=tuition_fees_category,
            amount=tuition_fees_amount,
            college_status=college_status,
            name="tuition & fees"
        )

    ################ room and board
    try:
        room = AidRawData.objects.get(college_status=college_status, aid_category=room_category)
    except:
        room = None

    try:
        meals = AidRawData.objects.get(college_status=college_status, aid_category=meals_category)
    except:
        meals = None

    # use raw data if that exists
    if room is not None:
        room_meals_name = "room & board"
        room_meals_amount = room.amount

        if meals is not None:
            room_meals_amount += meals.amount

    else:
        if college_status.residency == "oncampus":
            room_meals_amount = ipeds.room_on_campus
            room_meals_name = "on campus room & board"

        elif college_status.residency == "offcampus not with family":
            room_meals_amount = ipeds.room_off_campus_not_with_family
            room_meals_name = "off-campus not with family room & board"

    # update it if it already exists
    try:
        final_room_meals = AidFinalData.objects.get(
            aid_category=room_board_category,
            college_status=college_status,
        )

        if final_room_meals.amount != room_meals_amount:
            final_room_meals.update(amount=room_meals_amount)

    # create a new one if it doesn't
    except:
        AidFinalData.objects.create(
            aid_category=room_board_category,
            amount=room_meals_amount,
            college_status=college_status,
            name=room_meals_name
        )

    direct_cost = tuition_fees_amount + room_meals_amount

    ################ personal expenses
    # see if it exists
    try:
        final_personal_expenses = AidFinalData.objects.get(
            aid_category=personal_expenses_category,
            college_status=college_status,
        )

    # create a new one if it doesn't
    except:
        AidFinalData.objects.create(
            aid_category=personal_expenses_category,
            amount=5000,
            college_status=college_status,
            name="standard personal expenses"
        )

    # add 5,000 for indirect costs
    if direct_cost is not None:
        total_cost = direct_cost + 5000

    # calculate the total grant amount on the award letter
    grant_categories_keys = grant_categories.values_list('id', flat=True)
    grants = AidRawData.objects.filter(college_status=college_status, aid_category__in=grant_categories_keys)

    if grants.exists():
        final_grants = AidFinalData.objects.filter(college_status=college_status, aid_category__in=grant_categories_keys)

        if final_grants.exists():
            final_grants.delete()

        for grant in grants:
            total_aid += grant.amount
            AidFinalData.objects.create(
                aid_category=grant.aid_category,
                amount=grant.amount,
                college_status=grant.college_status,
                name=grant.name
            )

    # calculates net price
    net_price = total_cost - total_aid

    # save the aid summary data
    college_status.award_total_costs = total_cost
    college_status.award_total_grants = total_aid
    college_status.award_net_price = net_price
    college_status.save()

    ################ loans
    loan_categories_keys = loan_categories.values_list('id', flat=True)
    loans = AidRawData.objects.filter(college_status=college_status, aid_category__in=loan_categories_keys)

    if loans.exists():
        final_loans = AidFinalData.objects.filter(college_status=college_status, aid_category__in=loan_categories_keys)

        if final_loans.exists():
            final_loans.delete()

        for loan in loans:
            AidFinalData.objects.create(
                aid_category=loan.aid_category,
                amount=loan.amount,
                college_status=loan.college_status,
                name=loan.name
            )

    ################ work study
    try:
        work_study = AidRawData.objects.get(college_status=college_status, aid_category=work_study_category)
    except:
        word_study = None

    if work_study is not None:
        # update it if it already exists
        try:
            final_work_study = AidFinalData.objects.get(
                aid_category=work_study_category,
                college_status=college_status
            )

            if final_work_study.amount != work_study.amount:
                final_work_study.update(amount=work_study.amount)

        # create a new one if it doesn't
        except:
            AidFinalData.objects.create(
                aid_category=work_study_category,
                amount=work_study.amount,
                college_status=college_status,
                name=work_study.name
            )

    # caclulate the most affordable option for the user
    college_statuses = CollegeStatus.objects.filter(user=user).exclude(award_status="").order_by('award_net_price')

    first_record = True
    for record in college_statuses:
        if first_record == True and record.award_net_price is not None:
            record.most_affordable = True
            record.save()
            first_record = False
        else:
            record.most_affordable = False
            record.save()
