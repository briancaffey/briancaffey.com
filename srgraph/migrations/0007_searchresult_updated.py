# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-14 01:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srgraph', '0006_auto_20170514_0029'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchresult',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
