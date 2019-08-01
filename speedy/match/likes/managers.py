from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from speedy.core.base.models import BaseManager
from speedy.core.accounts.utils import get_site_profile_model
from speedy.core.accounts.models import User


class UserLikeManager(BaseManager):
    def add_like(self, from_user, to_user):
        from speedy.core.blocks.models import Block

        if (from_user == to_user):
            raise ValidationError(_("Users cannot like themselves."))

        if (self.filter(from_user=from_user, to_user=to_user).exists()):
            raise ValidationError(_("User already likes other user."))

        if (Block.objects.there_is_block(user_1=from_user, user_2=to_user)):
            raise ValidationError(_("User cannot like a blocked user."))

        self.create(from_user=from_user, to_user=to_user)

    def remove_like(self, from_user, to_user):
        self.filter(from_user=from_user, to_user=to_user).delete()

    def get_like_list_to_queryset(self, user):
        SiteProfile = get_site_profile_model()
        table_name = SiteProfile._meta.db_table

        # filter out users that are only active in another language
        liked_users = User.objects.filter(pk__in=self.filter(from_user=user).values_list('to_user_id', flat=True))
        liked_users = [u.pk for u in liked_users if (u.speedy_match_profile.is_active)]

        extra_select = {
            'last_visit': 'SELECT last_visit FROM {} WHERE user_id = likes_userlike.to_user_id'.format(table_name),
        }
        return self.filter(from_user=user).filter(to_user__in=liked_users).extra(select=extra_select).order_by('-last_visit')

    def get_like_list_from_queryset(self, user):
        SiteProfile = get_site_profile_model()
        table_name = SiteProfile._meta.db_table

        # filter out users that are only active in another language
        who_likes_me = User.objects.filter(pk__in=self.filter(to_user=user).values_list('from_user_id', flat=True))
        who_likes_me = [u.pk for u in who_likes_me if (u.speedy_match_profile.is_active)]

        extra_select = {
            'last_visit': 'SELECT last_visit FROM {} WHERE user_id = likes_userlike.from_user_id'.format(table_name),
        }
        return self.filter(to_user=user).filter(from_user__in=who_likes_me).extra(select=extra_select).order_by('-last_visit')

    def get_like_list_mutual_queryset(self, user):
        SiteProfile = get_site_profile_model()
        table_name = SiteProfile._meta.db_table

        # filter out users that are only active in another language
        who_likes_me = User.objects.filter(pk__in=self.filter(to_user=user).values_list('from_user_id', flat=True))
        who_likes_me = [u.pk for u in who_likes_me if (u.speedy_match_profile.is_active)]

        extra_select = {
            'last_visit': 'SELECT last_visit FROM {} WHERE user_id = likes_userlike.to_user_id'.format(table_name),
        }
        return self.filter(from_user=user, to_user_id__in=who_likes_me).extra(select=extra_select).order_by('-last_visit')

