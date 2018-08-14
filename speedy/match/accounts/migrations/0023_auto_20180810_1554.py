# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-10 12:54
from __future__ import unicode_literals

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import speedy.match.accounts.models


class Migration(migrations.Migration):

    dependencies = [
        ('match_accounts', '0022_auto_20180707_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteprofile',
            name='children',
            field=models.TextField(blank=True, null=True, verbose_name='Do you have children? How many?'),
        ),
        migrations.AlterField(
            model_name='siteprofile',
            name='children_en',
            field=models.TextField(blank=True, null=True, verbose_name='Do you have children? How many?'),
        ),
        migrations.AlterField(
            model_name='siteprofile',
            name='children_he',
            field=models.TextField(blank=True, null=True, verbose_name='Do you have children? How many?'),
        ),
        migrations.AlterField(
            model_name='siteprofile',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='city or locality'),
        ),
        migrations.AlterField(
            model_name='siteprofile',
            name='city_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='city or locality'),
        ),
        migrations.AlterField(
            model_name='siteprofile',
            name='city_he',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='city or locality'),
        ),
        migrations.AlterField(
            model_name='siteprofile',
            name='diet_match',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=speedy.match.accounts.models.SiteProfile.diet_match_default, verbose_name='diet match'),
        ),
        migrations.AlterField(
            model_name='siteprofile',
            name='gender_to_match',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.SmallIntegerField(), blank=True, default=speedy.match.accounts.models.SiteProfile.gender_to_match_default, null=True, size=3, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='siteprofile',
            name='height',
            field=models.SmallIntegerField(blank=True, help_text='cm', null=True, verbose_name='height'),
        ),
        migrations.AlterField(
            model_name='siteprofile',
            name='marital_status',
            field=models.SmallIntegerField(choices=[(0, 'Please select...'), (1, 'Single'), (2, 'Divorced'), (3, 'Widowed'), (4, 'In a relatioship'), (5, 'In an open relationship'), (6, "It's complicated"), (7, 'Separated'), (8, 'Married')], default=0, verbose_name='marital status'),
        ),
        migrations.AlterField(
            model_name='siteprofile',
            name='marital_status_match',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=speedy.match.accounts.models.SiteProfile.marital_status_match_default, verbose_name='marital status match'),
        ),
        migrations.AlterField(
            model_name='siteprofile',
            name='match_description',
            field=models.TextField(blank=True, null=True, verbose_name='My ideal match'),
        ),
        migrations.AlterField(
            model_name='siteprofile',
            name='match_description_en',
            field=models.TextField(blank=True, null=True, verbose_name='My ideal match'),
        ),
        migrations.AlterField(
            model_name='siteprofile',
            name='match_description_he',
            field=models.TextField(blank=True, null=True, verbose_name='My ideal match'),
        ),
        migrations.AlterField(
            model_name='siteprofile',
            name='max_age_match',
            field=models.SmallIntegerField(default=180, verbose_name='maximal age to match'),
        ),
        migrations.AlterField(
            model_name='siteprofile',
            name='min_age_match',
            field=models.SmallIntegerField(default=0, verbose_name='minimal age to match'),
        ),
        migrations.AlterField(
            model_name='siteprofile',
            name='more_children',
            field=models.TextField(blank=True, null=True, verbose_name='Do you want (more) children?'),
        ),
        migrations.AlterField(
            model_name='siteprofile',
            name='more_children_en',
            field=models.TextField(blank=True, null=True, verbose_name='Do you want (more) children?'),
        ),
        migrations.AlterField(
            model_name='siteprofile',
            name='more_children_he',
            field=models.TextField(blank=True, null=True, verbose_name='Do you want (more) children?'),
        ),
        migrations.AlterField(
            model_name='siteprofile',
            name='profile_description',
            field=models.TextField(blank=True, null=True, verbose_name='Few words about me'),
        ),
        migrations.AlterField(
            model_name='siteprofile',
            name='profile_description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Few words about me'),
        ),
        migrations.AlterField(
            model_name='siteprofile',
            name='profile_description_he',
            field=models.TextField(blank=True, null=True, verbose_name='Few words about me'),
        ),
        migrations.AlterField(
            model_name='siteprofile',
            name='smoking',
            field=models.SmallIntegerField(choices=[(0, 'Please select...'), (1, 'No'), (2, 'Sometimes'), (3, 'Yes')], default=0, verbose_name='smoking status'),
        ),
        migrations.AlterField(
            model_name='siteprofile',
            name='smoking_match',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=speedy.match.accounts.models.SiteProfile.smoking_status_match_default, verbose_name='smoking status match'),
        ),
    ]