import logging

from django.contrib import messages
from django.contrib.sites.models import Site
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.utils.translation import pgettext_lazy
from django.utils.translation import ugettext as _

from speedy.core.accounts.views import IndexView as CoreIndexView, ActivateSiteProfileView as CoreActivateSiteProfileView, EditProfileNotificationsView as CoreEditProfileNotificationsView
from speedy.match.accounts import utils
from speedy.match.accounts.models import SiteProfile as SpeedyMatchSiteProfile

from .forms import ProfileNotificationsForm

logger = logging.getLogger(__name__)


class IndexView(CoreIndexView):
    registered_redirect_to = 'matches:list'


class ActivateSiteProfileView(CoreActivateSiteProfileView):
    def get_context_data(self, **kwargs):
        logger.debug('HERE: get_context_data: kwargs: %s', kwargs)
        cd = super().get_context_data(**kwargs)
        cd.update({
            'steps_range': list(utils.get_steps_range()),
            'current_step': self.step,
            'previous_step': self.step - 1,
        })
        return cd

    def get_form_kwargs(self):
        logger.debug('HERE: get_form_kwargs')
        kwargs = super().get_form_kwargs()
        kwargs['step'] = self.step
        return kwargs

    # ~~~~ TODO: Read about dispatch and request lifecycle to understand why 'step' is wrong
    def dispatch(self, request, *args, **kwargs):
        if (not (self.request.user.is_authenticated)):
            return super().dispatch(request=request, *args, **kwargs)
        logger.debug('HERE: dispatch: args: %s, kwargs: %s', args, kwargs)
        try:
            if (not ('step' in kwargs)):
                logger.debug("dispatch: 'step' is missing from kwargs, adding it")
                logger.debug("self.request.user.speedy_match_profile.activation_step: %d", self.request.user.speedy_match_profile.activation_step)
                kwargs['step'] = self.request.user.speedy_match_profile.activation_step

            self.step = int(kwargs['step'])
            logger.debug("dispatch: self.step: %i" , self.step)
        except (ValueError):
            logger.debug("dispatch: kwargs['step']: %s, is not a number")
            logger.debug("dispatch: self.request.user.speedy_match_profile.activation_step: %i" , self.request.user.speedy_match_profile.activation_step)
            return redirect(to='accounts:activate', step=self.request.user.speedy_match_profile.activation_step)
        return super().dispatch(request=request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        # ~~~~ TODO: redirect all URLs of this view and never use the default URL directly.
        logger.debug('HERE: get: kwargs: %s, self.step: %i', kwargs, self.step)
        logger.debug('get: request.user.is_active ? %s' , request.user.is_active)
        if (not (request.user.is_active)):
            logger.debug('get: inside "if (not (request.user.is_active)):" self.template_name: %s', self.template_name)
            return render(request=self.request, template_name=self.template_name, context={})
        if (self.step == 1):
            logger.debug('get: inside "if (not (request.user.is_active)):" self.template_name: %s', self.template_name)
            return redirect(to='accounts:edit_profile')
        if (self.step >= len(SpeedyMatchSiteProfile.settings.SPEEDY_MATCH_SITE_PROFILE_FORM_FIELDS)):
            logger.debug('get: inside "if (self.step >= len(SpeedyMatchSiteProfile.settings.SPEEDY_MATCH_SITE_PROFILE_FORM_FIELDS)):"')
            return redirect(to='matches:list')
        logger.debug('get: did not get into "if (self.step >= len(SpeedyMatchSiteProfile.settings.SPEEDY_MATCH_SITE_PROFILE_FORM_FIELDS)):"')
        # else:
        #     step, errors = self.request.user.speedy_match_profile.validate_profile_and_activate()
        #     if (self.request.user.speedy_match_profile.activation_step == 0) and (
        #         step == len(SpeedyMatchSiteProfile.settings.SPEEDY_MATCH_SITE_PROFILE_FORM_FIELDS)) and not self.request.user.has_confirmed_email():
        #         return redirect(to=reverse_lazy('accounts:edit_profile_credentials'))
        return super().get(request=self.request, *args, **kwargs)

    def get_account_activation_url(self):
        return reverse_lazy('accounts:activate', kwargs={'step': self.step})

    def get_success_url(self):
        if (self.step >= len(SpeedyMatchSiteProfile.settings.SPEEDY_MATCH_SITE_PROFILE_FORM_FIELDS)):
            if (self.request.user.has_confirmed_email()):
                return reverse_lazy('matches:list', kwargs={'step': self.step})
            else:
                return reverse_lazy('accounts:edit_profile_emails', kwargs={'step': self.step})
        else:
            return reverse_lazy('accounts:activate', kwargs={'step': self.step + 1})

    def form_valid(self, form):
        super().form_valid(form=form)
        site = Site.objects.get_current()
        if (self.object.is_active):
            messages.success(request=self.request, message=pgettext_lazy(context=self.request.user.get_gender(), message='Welcome to {site_name}!').format(site_name=_(site.name)))
        if (self.request.user.speedy_match_profile.is_active):
            return redirect(to=reverse_lazy('matches:list'))
        else:
            return redirect(to=self.get_success_url())


class EditProfileNotificationsView(CoreEditProfileNotificationsView):
    form_class = ProfileNotificationsForm


