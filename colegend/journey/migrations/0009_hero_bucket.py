# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-28 23:50
from __future__ import unicode_literals

import colegend.core.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journey', '0008_hero_resources'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='bucket',
            field=colegend.core.fields.MarkdownField(blank=True, help_text='bucket list'),
        ),
    ]