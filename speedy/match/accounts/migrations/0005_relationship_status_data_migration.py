# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-04 12:26
from __future__ import unicode_literals

from django.db import migrations

from speedy.core.base.utils import string_is_not_empty


def forwards_func(apps, schema_editor):
    from django.conf import settings as django_settings

    from speedy.core.base.utils import to_attribute
    from speedy.match.accounts.models import SiteProfile as SpeedyMatchSiteProfile1
    SpeedyMatchSiteProfile = apps.get_model("match_accounts", "SiteProfile")
    for speedy_match_profile in SpeedyMatchSiteProfile.objects.all():
        speedy_match_profile.relationship_status_match = SpeedyMatchSiteProfile1.relationship_status_match_default()
        speedy_match_profile.active_languages = ""
        speedy_match_profile.activation_step = 2
        for language_code, language_name in django_settings.LANGUAGES:
            setattr(speedy_match_profile, to_attribute(name='activation_step', language_code=language_code), 2)
        speedy_match_profile.save()
        print (speedy_match_profile.pk, speedy_match_profile.relationship_status_match, speedy_match_profile.active_languages, speedy_match_profile.activation_step, speedy_match_profile.activation_step_en, speedy_match_profile.activation_step_he)


def backwards_func(apps, schema_editor):
    SpeedyMatchSiteProfile = apps.get_model("match_accounts", "SiteProfile")
    for speedy_match_profile in SpeedyMatchSiteProfile.objects.all():
        print (speedy_match_profile.pk, speedy_match_profile.relationship_status_match, speedy_match_profile.active_languages, speedy_match_profile.activation_step_en, speedy_match_profile.activation_step_he)


class Migration(migrations.Migration):

    dependencies = [
        ('match_accounts', '0004_auto_20190731_0948'),
    ]

    operations = [
        migrations.RunPython(forwards_func, backwards_func),
    ]
