# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-09 23:48
from __future__ import unicode_literals

import colegend.core.fields
import colegend.core.validators
import datetime
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('dayentries', '0006_auto_20160205_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dayentry',
            name='date',
            field=colegend.core.fields.DateField(default=datetime.datetime.today,
                                                 validators=[colegend.core.validators.validate_date_present_or_past]),
        ),
    ]
