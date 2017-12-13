# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-12 16:11
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arcade', '0004_auto_20171212_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='adventurereview',
            name='rating',
            field=models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='rating'),
            preserve_default=False,
        ),
    ]
