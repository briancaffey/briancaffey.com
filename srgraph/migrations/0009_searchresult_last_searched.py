# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-14 16:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('srgraph', '0008_auto_20170514_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchresult',
            name='last_searched',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
