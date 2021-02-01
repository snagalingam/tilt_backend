from colleges.models import CollegeStatus, Ipeds
from financial_aid.models import AidCategory, AidData
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver


@receiver(post_save, sender=AidData, dispatch_uid='calculate_aid_summary')
def calculate_aid_summary(sender, instance, **kwargs):
    college_status = instance.college_status

    total_aid = 0
    total_cost = 0

    # calculate the total cost amount
    direct_cost_categories = AidCategory.objects.filter(primary="cost", secondary="direct")
    direct_cost_categories_keys = direct_cost_categories.values_list('id', flat=True)

    costs = AidData.objects.filter(college_status=college_status, aid_category__in=direct_cost_categories_keys)

    if costs.exists():
        direct_cost = 0
        for cost in costs:
            direct_cost += cost.amount

    else:
        # get ipeds object for tuition
        ipeds = Ipeds.objects.get(college=college_status.college)

        # tuition and fees
        if college_status.in_state_tuition == "yes":
            tuition_amount = ipeds.tuition_in_state
            tuition_name = "in-state tuition"
            fees_amount = ipeds.fees_in_state
            fees_name = "in-state fees"

        else:
            tuition_amount = ipeds.tuition_out_of_state
            tuition_name = "out-of-state tuition"
            fees_amount = ipeds.fees_out_of_state
            fees_name = "out-of-state fees"

        AidData.objects.create(
            aid_category=AidCategory.objects.get(name="tuition"),
            amount=tuition_amount,
            college_status=college_status,
            name=tuition_name,
            other_source="ipeds"
        )

        AidData.objects.create(
            aid_category=AidCategory.objects.get(name="fees"),
            amount=fees_amount,
            college_status=college_status,
            name=fees_name,
            other_source="ipeds"
        )

        # room and board and other expenses
        if college_status.residency == "oncampus":
            other_expenses_amount = ipeds.other_expenses_on_campus
            other_expenses_name = "on-campus other expenses"
            room_amount = ipeds.room_on_campus
            room_name = "on campus room & board"

            AidData.objects.create(
                aid_category=AidCategory.objects.get(name="room"),
                amount=room_amount,
                college_status=college_status,
                name=room_name,
                other_source="ipeds"
            )

        elif college_status.residency == "offcampus not with family":
            other_expenses_amount = ipeds.other_expenses_off_campus_not_with_family
            other_expenses_name = "off-campus not with family other expenses"
            room_amount = ipeds.room_off_campus_not_with_family
            room_name = "off-campus not with family room & board"

            AidData.objects.create(
                aid_category=AidCategory.objects.get(name="off campus housing"),
                amount=room_amount,
                college_status=college_status,
                name=room_name,
                other_source="ipeds"
            )

        elif college_status.residency == "offcampus with family":
            other_expenses_amount = ipeds.other_expenses_off_campus_with_family
            other_expenses_name = "off-campus with family other expenses"
            room_amount = 0


        AidData.objects.create(
            aid_category=AidCategory.objects.get(name="personal expenses"),
            amount=other_expenses_amount,
            college_status=college_status,
            name=other_expenses_name,
            other_source="ipeds"
        )

        direct_cost = tuition_amount + fees_amount + room_amount

    # add 5,000 for indirect costs
    if direct_cost is not None:
        total_cost = direct_cost + 5000

    # calculate the total grant amount on the award letter
    grant_categories = AidCategory.objects.filter(primary="grant")
    grant_categories_keys = grant_categories.values_list('id', flat=True)

    try:
        grants = AidData.objects.filter(college_status=college_status, aid_category__in=grant_categories_keys)
        for grant in grants:
            total_aid += grant.amount
    except:
        grants = None

    # calculates net price
    net_price = total_cost - total_aid

    # save the aid summary data
    college_status.award_total_costs = total_cost
    college_status.award_total_grants = total_aid
    college_status.award_net_price = net_price
    college_status.save()

    # caclulate the most affordable option for the user
    user = college_status.user
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

@receiver(post_delete, sender=AidData, dispatch_uid='update_aid_summary')
def update_aid_summary(sender, instance, **kwargs):
    college_status = instance.college_status

    try:
        aid_data = AidData.objects.filter(college_status=college_status)
        calculate_aid_summary(sender=AidData, instance=instance)

    # if there is no more Aid Data for this college status, delete everything
    except:
        college_status.award_status = ""
        college_status.award_total_costs = 0
        college_status.award_total_grants = 0
        college_status.award_net_price = 0
        college_status.most_affordable = False
        college_status.save()

        # update most affordable option
        user = college_status.user
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
