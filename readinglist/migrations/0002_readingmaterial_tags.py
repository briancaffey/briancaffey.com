# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-10 14:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readinglist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='readingmaterial',
            name='tags',
            field=models.CharField(default='django', max_length=100),
            preserve_default=False,
        ),
    ]
