# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-08 16:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 8, 16, 11, 33, 750284, tzinfo=utc)),
        ),
    ]
