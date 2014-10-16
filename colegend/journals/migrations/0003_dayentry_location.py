# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journals', '0002_auto_20140908_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='dayentry',
            name='location',
            field=models.CharField(default='', max_length=100),
            preserve_default=True,
        ),
    ]
