# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-06 11:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sys_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 6, 11, 2, 31, 120983), null=True),
        ),
    ]
