################################################################################
# Check the raw aid data that was parsed
################################################################################
def check_aid_raw_data(aid_data, aid_categories):
    errors = []

    ################ check that there are no duplicates
    # cost categories
    cost_categories = aid_categories.filter(primary="cost")
    total_direct_cost_amount = 0
    total_indirect_cost_amount = 0

    for category in cost_categories:
        # check that there is only one row assigned each category
        count = aid_data.filter(aid_category=category).count()

        if count > 1:
            errors.append({
                "type": f"Multiple data points for {category.name}",
                "message": f"There are {count} data points for {category.name}"
            })

        # add to direct total
        if category.secondary == "direct" and count > 0:
            data = aid_data.filter(aid_category=category)

            for row in data:
                total_direct_cost_amount += row.amount

        # add to indirect total
        elif category.secondary == "indirect" and count > 0:
            data = aid_data.filter(aid_category=category)

            for row in data:
                total_indirect_cost_amount += row.amount

    total_direct_and_indirect_costs_amount = total_direct_cost_amount + total_indirect_cost_amount

    # grant categories excluding other
    grant_categories = aid_categories.filter(primary="grant").exclude(secondary="other")
    total_grant_amount = 0

    for category in grant_categories:
        count = aid_data.filter(aid_category=category).count()

        if count > 1:
            errors.append({
                "type": f"Multiple data points for {category.name}",
                "message": f"There are {count} data points for {category.name}"
            })

        # add to grant total
        if count > 0:
            data = aid_data.filter(aid_category=category)

            for row in data:
                total_grant_amount += row.amount

    # loan categories
    loan_categories = aid_categories.filter(primary="loan")
    total_loan_amount = 0

    for category in loan_categories:
        count = aid_data.filter(aid_category=category).count()

        if count > 1:
            errors.append({
                "type": f"Multiple data points for {category.name}",
                "message": f"There are {count} data points for {category.name}"
            })

        # add to loan total
        if count > 0:
            data = aid_data.filter(aid_category=category)

            for row in data:
                total_loan_amount += row.amount

    # work study
    work_study_category = aid_categories.get(primary="work study")
    work_study_count = aid_data.filter(aid_category=work_study_category).count()
    total_work_study_amount = 0

    if work_study_count > 1:
        errors.append({
            "type": f"Multiple data points for {work_study_category.name}",
            "message": f"There are {work_study_count} data points for {work_study_category.name}"
        })

    if work_study_count > 0:
        data = aid_data.filter(aid_category=work_study_category)

        for row in data:
            total_work_study_amount += row.amount

    total_grant_and_loan_amount = total_grant_amount + total_loan_amount
    total_grant_and_loan_and_work_study_amount = total_grant_amount + total_loan_amount + total_work_study_amount

    ################ check that total costs only have one row
    total_categories = aid_categories.filter(primary="total")
    total_aid_defined_by_school_category = aid_categories.filter(primary="total aid defined by school")
    total_direct_cost_category = aid_categories.get(name="total direct cost")
    total_direct_and_indirect_costs_category = aid_categories.get(name="total direct and indirect costs")
    total_indirect_cost_category = aid_categories.get(name="total indirect cost")
    total_grant_category = aid_categories.get(name="total grants")
    total_grant_and_loan_category = aid_categories.get(name="total grants and loans")
    total_grant_and_loan_and_work_study_category = aid_categories.get(name="total grants and loans and work study")
    total_cost_defined_by_school_category = aid_categories.get(name="total cost defined by school")
    total_loan_category = aid_categories.get(name="total loans")

    total_aid_defined_by_school_count = 0
    total_cost_defined_by_school_count = 0
    total_direct_cost_count = 0
    total_direct_and_indirect_costs_count = 0
    total_grant_count = 0
    total_indirect_cost_count = 0
    total_loan_count = 0

    for category in total_categories:
        count = aid_data.filter(aid_category=category).count()

        if category == total_aid_defined_by_school_category:
            total_aid_defined_by_school_count = count

        elif category == total_cost_defined_by_school_category:
            total_cost_defined_by_school_count = count

        elif category == total_direct_cost_category:
            total_direct_cost_count = count

        elif category == total_direct_and_indirect_costs_category:
            total_direct_and_indirect_costs_count = count

        elif category == total_grant_category:
            total_grant_count = count

        elif category == total_indirect_cost_category:
            total_indirect_cost_count = count

        elif category == total_loan_category:
            total_loan_count = count

        if count > 1:
            errors.append({
                "type": f"Multiple data points for {category.name}",
                "message": f"There are {count} data points for {category.name}"
            })

    ################ total costs
    # total direct cost - check that total adds up to what we pulled
    if total_direct_cost_count == 1:
        total_direct_cost = aid_data.get(aid_category=total_direct_cost_category)

        if total_direct_cost_amount != total_direct_cost.amount:
            errors.append({
                "type": f"Direct cost data points don't equal total direct cost pulled from award letter",
                "message":
                    f"Direct cost data points add up to {total_direct_cost_amount} while row with " \
                    f"total direct cost amount is {total_direct_cost.amount}"
            })

    # total indirect cost - check that total adds up to what we pulled
    if total_indirect_cost_count == 1:
        total_indirect_cost = aid_data.get(aid_category=total_indirect_cost_category)

        if total_indirect_cost_amount != total_indirect_cost.amount:
            errors.append({
                "type": f"Direct cost data points don't equal total direct cost pulled from award letter",
                "message":
                    f"Direct cost data points add up to {total_direct_cost_amount} while row with " \
                    f"total direct cost amount is {total_direct_cost.amount}"
            })

    # total cost defined by school - check that total adds up to what we pulled
    if total_cost_defined_by_school_count == 1:

        if total_cost_defined_by_school.amount == total_direct_cost_amount and total_direct_cost_count == 0:
            total_cost_defined_by_school.category = total_direct_cost_category
            total_cost_defined_by_school.save()

        elif total_cost_defined_by_school.amount == total_indirect_cost_amount and total_indirect_cost_count == 0:
            total_cost_defined_by_school.category = total_indirect_cost_category
            total_cost_defined_by_school.save()

        elif total_cost_defined_by_school.amount == total_direct_and_indirect_costs_amount and total_direct_and_indirect_costs_count == 0:
            total_cost_defined_by_school.category = total_direct_and_indirect_costs_category
            total_cost_defined_by_school.save()

        else:
            errors.append({
                "type": f"Total cost defined by school didn't add up to direct and\or indirect costs",
                "message":
                    f"Total costs defined by school was {total_cost_defined_by_school.amount} but " \
                    f"total direct cost was {total_direct_cost_amount} and total indirect cost was " \
                    f"{total_indirect_cost_amount}. Total of both was {total_direct_and_indirect_costs_amount}."
            })

    ################ total grants
    if total_grant_count == 1:
        total_grant = aid_data.get(aid_category=total_grant_category)

        if total_grant_amount != total_grant.amount:
            errors.append({
                "type": f"Grant data points don't equal total grant amount pulled from award letter",
                "message":
                    f"Grant data points add up to {total_grant_amount} while row with " \
                    f"total grant amount is {total_grant.amount}."
            })

    ################ total loans
    if total_loan_count == 1:
        total_loan = aid_data.get(aid_category=total_loan_category)

        if total_loan_amount != total_loan.amount:
            errors.append({
                "type": f"Loan data points don't equal total loan amount pulled from award letter",
                "message":
                    f"Loan data points add up to {total_loan_amount} while row with " \
                    f"total loan amount is {total_loan.amount}"
            })

    ################ total aid
    if total_aid_defined_by_school_count == 1:
        total_aid = aid_data.get(aid_category=total_aid_defined_by_school_category)

        if total_aid.amount == total_grant_amount and total_grant_count == 0:
            total_aid.category = total_grant_category
            total_aid.save()

        elif total_aid.amount == total_loan_amount and total_loan_count == 0:
            total_aid.category = total_loan_category
            total_aid.save()

        elif total_aid.amount == total_ and total_loan_count == 0:
            total_aid.category = total_loan_category
            total_aid.save()

        elif total_aid.amount == total_grant_and_loan_amount:
            total_aid.category = total_grant_and_loan_category
            total_aid.save()

        elif total_aid.amount == total_grant_and_loan_and_work_study_amount:
            total_aid.category = total_grant_and_loan_and_work_study_category
            total_aid.save()

        else:
            errors.append({
                "type": f"Total aid defined by school didn't add up to grants, loans, and work study",
                "message":
                    f"Total aid defined by school was {total_aid.amount} but " \
                    f"total grants was {total_grant_amount} and total loans was " \
                    f"{total_loan_amount} and work study was {total_work_study_amount}."
            })

    ################ check that net price categories only have one row
    net_price_categories = aid_categories.filter(primary="net price")
    net_price_after_grants_category = aid_categories.filter(primary="net price after grants")
    net_price_after_grants_and_loans_category = aid_categories.filter(primary="net price after grants and loans")
    net_price_after_grants_and_loans_and_work_study_category = aid_categories.filter(primary="net price after grants and loans")
    net_price_defined_by_school_category = aid_categories.filter(primary="net price defined by school")

    net_price_after_grants_count = 0
    net_price_after_grants_and_loans_count = 0
    net_price_after_grants_and_loans_and_work_study_count = 0
    net_price_defined_by_school_count = 0

    for category in net_price_categories:
        count = aid_data.filter(aid_category=category).count()

        if category == net_price_after_grants_category:
            net_price_after_grants_count = count

        elif category == net_price_after_grants_and_loans_category:
            net_price_after_grants_and_loans_count = count

        elif category == net_price_after_grants_and_loans_and_work_study_category:
            net_price_after_grants_and_loans_and_work_study_count = count

        elif category == net_price_defined_by_school_category:
            net_price_defined_by_school_count = count

        if count > 1:
            errors.append({
                "type": f"Multiple data points for {category.name}",
                "message": f"There are {count} data points for {category.name}"
            })

    return errors
