# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-03 02:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playquest', '0003_game_game_saved'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='game',
            options={'ordering': ['-game_created']},
        ),
        migrations.AddField(
            model_name='game',
            name='game_featured',
            field=models.BooleanField(default=False),
        ),
    ]