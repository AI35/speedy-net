# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-10 15:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('match_accounts', '0029_auto_20190709_2125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='siteprofile',
            name='city_en',
        ),
        migrations.RemoveField(
            model_name='siteprofile',
            name='city_he',
        ),
        migrations.RemoveField(
            model_name='siteprofile',
            name='marital_status',
        ),
        migrations.RemoveField(
            model_name='siteprofile',
            name='smoking_status',
        ),
    ]