# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-30 03:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hashtest', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hashitem',
            name='reference_id',
        ),
        migrations.AddField(
            model_name='hashitem',
            name='game_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
