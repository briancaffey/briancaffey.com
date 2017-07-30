# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-30 04:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('hashtest', '0005_hashitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='HashItemReferencingItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_uid', models.CharField(default=uuid.uuid4, max_length=40)),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hashtest.HashItem')),
            ],
        ),
    ]