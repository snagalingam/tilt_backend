import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model
from .models import Budget
from colleges.models import Status

class BudgetType(DjangoObjectType):
    class Meta:
        model = Budget
        fields = "__all__"

class Query(graphene.ObjectType):
    budgets = graphene.List(BudgetType, limit=graphene.Int())

    budget_results_by_fields = graphene.List(
        BudgetType, 
        college_status_id=graphene.Int(),
        work_study=graphene.Int(),
        job=graphene.Int(),
        savings=graphene.Int(),
        family=graphene.Int(),
        other_scholarships=graphene.Int(),
        loan_subsideized=graphene.Int(),
        loan_unsubsideized=graphene.Int(),
        loan_plus=graphene.Int(),
        loan_private=graphene.Int(),
        loan_school=graphene.Int())

    def resolve_budgets(self, info, limit=None):
        qs = Budget.objects.all()[0:limit]
        return qs

    def resolve_budget_results_by_fields(root, info, **fields):
        qs = Budget.objects.filter(**fields)
        return qs

class CreateBudget(graphene.Mutation):
    budget = graphene.Field(BudgetType)

    class Arguments:
        college_status_id=graphene.Int()
        work_study=graphene.Int()
        job=graphene.Int()
        savings=graphene.Int()
        family=graphene.Int()
        other_scholarships=graphene.Int()
        loan_subsideized=graphene.Int()
        loan_unsubsideized=graphene.Int()
        loan_plus=graphene.Int()
        loan_private=graphene.Int()
        loan_school=graphene.Int()

    def mutate(
        self,
        info,
        college_status_id=None,
        work_study=None,
        job=None,
        savings=None,
        family=None,
        other_scholarships=None,
        loan_subsideized=None,
        loan_unsubsideized=None,
        loan_plus=None,
        loan_private=None,
        loan_school=None,
    ):

        college_status = Status.objects.get(pk=college_status_id)

        budget = Budget(
            college_status=college_status,
            work_study=work_study,
            job=job,
            savings=savings,
            family=family,
            other_scholarships=other_scholarships,
            loan_subsideized=loan_subsideized,
            loan_unsubsideized=loan_unsubsideized,
            loan_plus=loan_plus,
            loan_private=loan_private,
            loan_school=loan_school,
            )
        budget.save()
        return CreateBudget(budget=budget)

class UpdateBudget(graphene.Mutation):
    budget = graphene.Field(BudgetType)

    class Arguments:
        pk=graphene.ID()
        work_study=graphene.Int()
        job=graphene.Int()
        savings=graphene.Int()
        family=graphene.Int()
        other_scholarships=graphene.Int()
        loan_subsideized=graphene.Int()
        loan_unsubsideized=graphene.Int()
        loan_plus=graphene.Int()
        loan_private=graphene.Int()
        loan_school=graphene.Int()

    def mutate(
        self,
        info,
        pk=None,
        work_study=None,
        job=None,
        savings=None,
        family=None,
        other_scholarships=None,
        loan_subsideized=None,
        loan_unsubsideized=None,
        loan_plus=None,
        loan_private=None,
        loan_school=None,
    ):

        budget = Budget.objects.get(pk=pk)

        budget.work_study = work_study
        budget.job = job
        budget.savings = savings
        budget.family = family
        budget.other_scholarships = other_scholarships
        budget.loan_subsideized = loan_subsideized
        budget.loan_unsubsideized = loan_unsubsideized
        budget.loan_plus = loan_plus
        budget.loan_private = loan_private
        budget.loan_school = loan_school
        budget.save()
        return UpdateBudget(budget=budget)

class Mutation(graphene.ObjectType):
    create_budget = CreateBudget.Field()
    update_budget = UpdateBudget.Field()
