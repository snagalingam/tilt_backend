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
    other_loan_category = AidCategory.objects.get(name="other loan")
    personal_expenses_category = AidCategory.objects.get(name="standard personal expenses")
    plus_loan_category = AidCategory.objects.get(name="plus")
    room_category = AidCategory.objects.get(name="room")
    room_board_category = AidCategory.objects.get(name="room & board")
    subsidized_loan_category = AidCategory.objects.get(name="subsidized")
    tuition_category = AidCategory.objects.get(name="tuition")
    tuition_fees_category = AidCategory.objects.get(name="tuition & fees")
    unsubsidized_loan_category = AidCategory.objects.get(name="unsubsidized")
    work_study_category = AidCategory.objects.get(name="work study")

    # get ipeds object for costs
    ipeds = Ipeds.objects.get(college=college_status.college)

    ################ tuition and fees
    tuition_amount = None
    fees_amount = None
    tuition_fees_amount = None

    try:
        tuition = AidRawData.objects.get(college_status=college_status, aid_category=tuition_category)
    except:
        tuition = None

    try:
        fees = AidRawData.objects.get(college_status=college_status, aid_category=fees_category)
    except:
        fees = None

    # use data from award letter if that exists
    if tuition is not None:
        tuition_fees_amount = tuition.amount

        if fees is not None:
            tuition_fees_amount += fees.amount

    # otherwise, pull the data from ipeds
    else:
        # save flag that cost are missing on the award letter
        college_status.award_costs_missing = True
        college_status.save()

        # look at ipeds data
        if college_status.in_state_tuition == "yes":
            if ipeds.tuition_in_state is not None:
                tuition_amount = ipeds.tuition_in_state

            if ipeds.fees_in_state is not None:
                fees_amount = ipeds.fees_in_state

        else:
            if ipeds.tuition_out_of_state is not None:
                tuition_amount = ipeds.tuition_out_of_state

            if ipeds.fees_out_of_state is not None:
                fees_amount = ipeds.fees_out_of_state

        if tuition_amount is not None:
            tuition_fees_amount = tuition_amount
            if fees_amount is not None:
                tuition_fees_amount += fees_amount

    if tuition_fees_amount is not None:
        # update it if it already exists
        try:
            final_tuition_fees = AidFinalData.objects.get(
                aid_category=tuition_fees_category,
                college_status=college_status,
            )

            if final_tuition_fees.amount != tuition_fees_amount:
                final_tuition_fees.amount = tuition_fees_amount
                final_tuition_fees.save()

        # create a new one if it doesn't
        except:
            AidFinalData.objects.create(
                aid_category=tuition_fees_category,
                amount=tuition_fees_amount,
                college_status=college_status,
                name="Tuition & Fees"
            )

    ################ room and board
    room_amount = None
    meals_amount = None
    room_meals_amount = None

    try:
        room = AidRawData.objects.get(college_status=college_status, aid_category=room_category)
    except:
        room = None

    try:
        meals = AidRawData.objects.get(college_status=college_status, aid_category=meals_category)
    except:
        meals = None

    # use data from award letter if that exists
    if room is not None:
        room_meals_name = "On-Campus Housing & Meal Expenses"
        room_meals_amount = room.amount

        if meals is not None:
            room_meals_amount += meals.amount

    else:
        if college_status.residency == "offcampus not with family":
            if ipeds.room_off_campus_not_with_family is not None:
                room_meals_amount = ipeds.room_off_campus_not_with_family
                room_meals_name = "Off-Campus (not with Family) Housing & Meal Expenses"

        elif college_status.residency == "offcampus with family":
            room_meals_amount = 0
            room_meals_name = "Off-Campus (with Family) Housing & Meal Expenses"

        # assume on campus unless otherwise stated
        else:
            if ipeds.room_on_campus is not None:
                room_meals_amount = ipeds.room_on_campus
                room_meals_name = "On-Campus Housing & Meal Expenses"

    if room_meals_amount is not None:
        # update it if it already exists
        try:
            final_room_meals = AidFinalData.objects.get(
                aid_category=room_board_category,
                college_status=college_status,
            )

            if final_room_meals.amount != room_meals_amount:
                final_room_meals.amount = room_meals_amount
                final_room_meals.save()

        # create a new one if it doesn't
        except:
            AidFinalData.objects.create(
                aid_category=room_board_category,
                amount=room_meals_amount,
                college_status=college_status,
                name=room_meals_name
            )

    if tuition_fees_amount is not None and room_meals_amount is not None:
        direct_cost = tuition_fees_amount + room_meals_amount
    else:
        direct_cost = None

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
            name="Estimated Personal Expenses"
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
    # other loan
    try:
        other_loan = AidRawData.objects.get(college_status=college_status, aid_category=other_loan_category)
        AidFinalData.objects.create(
            aid_category=other_loan.aid_category,
            amount=other_loan.amount,
            college_status=other_loan.college_status,
            name=other_loan.name
        )
    except:
        pass

    # plus loan
    try:
        plus_loan = AidRawData.objects.get(college_status=college_status, aid_category=plus_loan_category)
        AidFinalData.objects.create(
            aid_category=plus_loan.aid_category,
            amount=plus_loan.amount,
            college_status=plus_loan.college_status,
            name="Federal Parent PLUS Loan"
        )
    except:
        pass

    # subsidized and unsbusidized loans
    try:
        subsidized_loan = AidRawData.objects.get(
            college_status=college_status,
            aid_category=subsidized_loan_category
        )
        AidFinalData.objects.create(
            aid_category=subsidized_loan.aid_category,
            amount=subsidized_loan.amount,
            college_status=subsidized_loan.college_status,
            name="Federal Subsidized Loan"
        )
        subsidized_amount = subsidized_loan.amount
    except:
        subsidized_amount = 0

    unsubsidized_amount = 5500 - subsidized_amount
    AidFinalData.objects.create(
        aid_category=unsubsidized_loan_category,
        amount=unsubsidized_amount,
        college_status=college_status,
        name="Federal Unsubsidized Loan"
    )

    ################ work study
    try:
        work_study = AidRawData.objects.get(college_status=college_status, aid_category=work_study_category)
    except:
        work_study = None

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
