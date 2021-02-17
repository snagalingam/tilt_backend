################################################################################
# Check the raw aid data that was parsed
################################################################################
def check_aid_raw_data(aid_data, aid_categories):
    errors = []

    ################ check that there are no duplicates
    # cost categories
    cost_categories = aid_categories.filter(primary="cost")
    for category in cost_categories:
        count = aid_data.filter(aid_category=category).count()

        if count > 1:
            errors.append({
                "type": f"Multiple data points for {category.name}",
                "message": f"There are {count} data points for {category.name}"
            })

    # grant categories excluding other
    grant_categories = aid_categories.filter(primary="grant").exclude(secondary="other")
    for category in grant_categories:
        count = aid_data.filter(aid_category=category).count()

        if count > 1:
            errors.append({
                "type": f"Multiple data points for {category.name}",
                "message": f"There are {count} data points for {category.name}"
            })

    # loan categories
    loan_categories = aid_categories.filter(primary="loan")
    for category in loan_categories:
        count = aid_data.filter(aid_category=category).count()

        if count > 1:
            errors.append({
                "type": f"Multiple data points for {category.name}",
                "message": f"There are {count} data points for {category.name}"
            })

    # work study
    work_study_category = aid_categories.filter(primary="work study")
    for category in work_study_category:
        count = aid_data.filter(aid_category=category).count()

        if count > 1:
            errors.append({
                "type": f"Multiple data points for {category.name}",
                "message": f"There are {count} data points for {category.name}"
            })

    ################ check that total matches to what we pulled
    direct_cost_categories = aid_categories.filter(primary="cost", secondary="direct")
    direct_cost_categories_keys = direct_cost_categories.values_list('id', flat=True)
    direct_cost_data = aid_data.filter(aid_category__in=direct_cost_categories_keys)

    total direct cost
    total indirect cost
    total cost defined by school

    total grants
    total loans
    total aid


    ################ check that net price matches to what we pulled

    net price after grants
    net price after grants and loans
    net price defined by school
