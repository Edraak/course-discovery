# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-08 10:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogs', '0001_squashed_0002_auto_20160327_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalog',
            name='include_archived',
            field=models.BooleanField(default=False, help_text='Include archived courses'),
        ),
    ]
