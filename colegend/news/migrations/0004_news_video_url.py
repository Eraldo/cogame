# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-29 12:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20171105_0244'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='video_url',
            field=models.URLField(blank=True, verbose_name='video url'),
        ),
    ]
