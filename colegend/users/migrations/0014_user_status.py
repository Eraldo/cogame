# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-16 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20170810_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.TextField(blank=True, verbose_name='status'),
        ),
    ]