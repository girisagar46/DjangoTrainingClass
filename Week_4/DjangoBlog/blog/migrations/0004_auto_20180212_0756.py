# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-12 02:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180210_1746'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('comment_text', models.TextField(max_length=200)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.AlterField(
            model_name='blog',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 12, 2, 11, 52, 962370, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.AddField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Blog'),
        ),
    ]
