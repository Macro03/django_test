# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-06 15:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sys_user', '0002_auto_20190706_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 6, 15, 26, 54, 343102), null=True),
        ),
    ]
