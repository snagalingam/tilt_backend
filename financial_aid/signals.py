from colleges.models import CollegeStatus, Scorecard
from financial_aid.models import AidCategory, AidData
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=AidData, dispatch_uid='calculate_aid_summary')
def calculate_aid_summary(sender, instance, **kwargs):
    college_status = instance.college_status

    award_scorecard_cost_estimate = ""
    total_aid = 0
    total_cost = 0

    # calculate the total cost amount
    direct_cost_categories = AidCategory.objects.filter(primary="cost", secondary="direct")
    direct_cost_categories_keys = direct_cost_categories.values_list('id', flat=True)

    costs = AidData.objects.filter(college_status=college_status, aid_category__in=direct_cost_categories_keys)
    print(costs)

    if costs.exists():
        direct_cost = 0
        for cost in costs:
            direct_cost += cost.amount

    else:
        # get scorecard object for tuition
        scorecard = Scorecard.objects.get(college=college_status.college)

        if college_status.in_state_tuition == "yes":
            direct_cost = scorecard.tuition_in_state

            if direct_cost is not None:
                award_scorecard_cost_estimate = "in-state tuition"

        else:
            direct_cost = scorecard.tuition_out_of_state

            if direct_cost is not None:
                award_scorecard_cost_estimate = "out-of-state tuition"

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
    college_status.award_scorecard_cost_estimate = award_scorecard_cost_estimate
    college_status.save()

    # caclulate the most affordable option for the user
    user = college_status.user

    # get all college statuses
    college_statuses = CollegeStatus.objects.filter(user=user).order_by('award_net_price')

    # save the first one as the most affordable option
    counter = 1
    for record in college_statuses:
        if counter == 1:
            record.most_affordable = True
            record.save()
        else:
            record.most_affordable = False
            record.save()
        counter += 1
