from django.utils.translation import gettext_lazy as _
from django.apps import AppConfig

from speedy.core.patches import locale_patches


class SpeedyCoreBaseConfig(AppConfig):
    name = 'speedy.core.base'
    verbose_name = _("Speedy Core Base App")
    label = 'base'

    def ready(self):
        locale_patches.patch()


