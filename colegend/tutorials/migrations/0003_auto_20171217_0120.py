# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-17 00:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0002_auto_20171108_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='video_url',
            field=models.URLField(blank=True, max_length=1000, verbose_name='video url'),
        ),
    ]