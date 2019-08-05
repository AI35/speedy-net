# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-03 10:27
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import speedy.match.accounts.models


class Migration(migrations.Migration):

    dependencies = [
        ('match_accounts', '0005_relationship_status_data_migration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='siteprofile',
            old_name='max_age_match',
            new_name='max_age_to_match',
        ),
        migrations.RenameField(
            model_name='siteprofile',
            old_name='min_age_match',
            new_name='min_age_to_match',
        ),
        migrations.AddField(
            model_name='siteprofile',
            name='diet_to_match',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.SmallIntegerField(), blank=True, default=speedy.match.accounts.models.SiteProfile.diet_to_match_default, null=True, size=3, verbose_name='Diet to match'),
        ),
        migrations.AddField(
            model_name='siteprofile',
            name='relationship_status_to_match',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.SmallIntegerField(), blank=True, default=speedy.match.accounts.models.SiteProfile.relationship_status_to_match_default, null=True, size=9, verbose_name='Relationship status to match'),
        ),
        migrations.AddField(
            model_name='siteprofile',
            name='smoking_status_to_match',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.SmallIntegerField(), blank=True, default=speedy.match.accounts.models.SiteProfile.smoking_status_to_match_default, null=True, size=3, verbose_name='Smoking status to match'),
        ),
    ]