# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-09 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outcomes', '0018_auto_20171117_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='outcome',
            name='completed_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='completed at'),
        ),
    ]
