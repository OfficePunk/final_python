# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-11-11 01:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20181111_0304'),
    ]

    operations = [
        migrations.AddField(
            model_name='userteam',
            name='max',
            field=models.IntegerField(blank=True, default=5, null=True),
        ),
    ]
