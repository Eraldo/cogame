# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-03 20:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0004_remove_experience_level'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experience',
            old_name='app',
            new_name='action',
        ),
    ]
