from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class FinancialAidConfig(AppConfig):
    name = 'financial_aid'
    verbose_name = _('financial aid')

    def ready(self):
        import financial_aid.signals
