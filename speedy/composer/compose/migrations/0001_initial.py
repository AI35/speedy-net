# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 11:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Accompaniment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('date_updated', models.DateTimeField(auto_now=True, db_index=True)),
            ],
            options={
                'verbose_name': 'accompaniment',
                'verbose_name_plural': 'accompaniments',
            },
        ),
        migrations.CreateModel(
            name='ChordsTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('date_updated', models.DateTimeField(auto_now=True, db_index=True)),
            ],
            options={
                'verbose_name': 'chords template',
                'verbose_name_plural': 'chords templates',
            },
        ),
        migrations.CreateModel(
            name='Composition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('date_updated', models.DateTimeField(auto_now=True, db_index=True)),
                ('tempo', models.SmallIntegerField(default=105, verbose_name='tempo')),
                ('public', models.BooleanField(default=False, verbose_name='public')),
                ('accompaniment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='compose.Accompaniment', verbose_name='accompaniment')),
                ('chords_template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='compose.ChordsTemplate', verbose_name='chords template')),
            ],
            options={
                'verbose_name': 'composition',
                'verbose_name_plural': 'compositions',
            },
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('date_updated', models.DateTimeField(auto_now=True, db_index=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'folder',
                'verbose_name_plural': 'folders',
            },
        ),
        migrations.AddField(
            model_name='composition',
            name='folder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='compose.Folder', verbose_name='folder'),
        ),
    ]