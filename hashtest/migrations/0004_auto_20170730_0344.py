# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-30 03:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hashtest', '0003_auto_20170730_0343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hashitem',
            name='item_owner',
        ),
        migrations.DeleteModel(
            name='HashItem',
        ),
    ]