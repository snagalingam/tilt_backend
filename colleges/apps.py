from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CollegesConfig(AppConfig):
    name = 'colleges'
    verbose_name = _('colleges')

    def ready(self):
        import colleges.signals
