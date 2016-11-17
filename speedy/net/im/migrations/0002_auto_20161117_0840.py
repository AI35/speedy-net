# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-17 08:40
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations
import speedy.core.models


class Migration(migrations.Migration):

    dependencies = [
        ('im', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='id',
            field=speedy.core.models.UDIDField(db_index=True, default=speedy.core.models.generate_udid, max_length=15, primary_key=True, serialize=False, unique=True, validators=[django.core.validators.RegexValidator(message='id contains illegal characters', regex='[0-9]')], verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='message',
            name='id',
            field=speedy.core.models.UDIDField(db_index=True, default=speedy.core.models.generate_udid, max_length=15, primary_key=True, serialize=False, unique=True, validators=[django.core.validators.RegexValidator(message='id contains illegal characters', regex='[0-9]')], verbose_name='ID'),
        ),
    ]
