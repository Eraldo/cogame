# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-13 22:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weekentries', '0006_auto_20170614_0017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weekentry',
            name='outcome_1',
        ),
        migrations.RemoveField(
            model_name='weekentry',
            name='outcome_2',
        ),
        migrations.RemoveField(
            model_name='weekentry',
            name='outcome_3',
        ),
        migrations.RemoveField(
            model_name='weekentry',
            name='outcome_4',
        ),
    ]
