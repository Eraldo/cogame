# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-08 22:27
from __future__ import unicode_literals

import colegend.core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('outcomes', '0009_auto_20170609_0027'),
        ('office', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Focus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scope', models.PositiveSmallIntegerField(choices=[(1, 'day'), (2, 'week'), (3, 'month'), (4, 'year')], default=1, verbose_name='scope')),
                ('start', models.DateField()),
                ('outcomes', models.ManyToManyField(related_name='focus', to='outcomes.Outcome')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(colegend.core.models.OwnedCheckMixin, models.Model),
        ),
    ]