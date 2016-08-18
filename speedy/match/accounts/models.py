from django.db import models
from django.utils.translation import ugettext_lazy as _

from speedy.net.accounts.models import SiteProfileBase, UserEmailAddress, ACCESS_FRIENDS


class SiteProfile(SiteProfileBase):
    access_account = ACCESS_FRIENDS
    public_email = models.ForeignKey(UserEmailAddress, verbose_name=_('public email'), blank=True, null=True, limit_choices_to={'is_confirmed': True}, on_delete=models.SET_NULL, related_name='+')
    notify_on_message = models.PositiveIntegerField(verbose_name=_('on new messages'), choices=SiteProfileBase.NOTIFICATIONS_CHOICES, default=SiteProfileBase.NOTIFICATIONS_ON)
    notify_on_like = models.PositiveIntegerField(verbose_name=_('on new likes'), choices=SiteProfileBase.NOTIFICATIONS_CHOICES, default=SiteProfileBase.NOTIFICATIONS_ON)

    class Meta:
        verbose_name = 'Speedy Match Profile'
        verbose_name_plural = 'Speedy Match Profiles'

