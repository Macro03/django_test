# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-07 23:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SceneApp', '0002_auto_20190707_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scene',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 7, 23, 27, 22, 504507), null=True, verbose_name='接入时间'),
        ),
    ]