# Generated by Django 2.0.4 on 2018-06-27 13:32

import colegend.core.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0009_auto_20171217_0120'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='events', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='content',
            field=colegend.core.fields.MarkdownField(verbose_name='content'),
        ),
    ]
