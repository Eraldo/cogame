# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-17 11:42
from __future__ import unicode_literals

import colegend.scopes.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outcomes', '0010_auto_20170617_1305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outcome',
            name='review',
        ),
        migrations.AddField(
            model_name='outcome',
            name='scope',
            field=colegend.scopes.models.ScopeField(choices=[('day', 'day'), ('week', 'week'), ('month', 'month'), ('year', 'year')], default='day', max_length=5, verbose_name='scope'),
        ),
    ]
