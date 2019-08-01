# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-31 06:48
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations
import speedy.match.accounts.models


class Migration(migrations.Migration):

    dependencies = [
        ('match_accounts', '0003_rename_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteprofile',
            name='relationship_status_match',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=speedy.match.accounts.models.SiteProfile.relationship_status_match_default, verbose_name='Relationship status match'),
        ),
    ]