# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-21 10:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DisStatus', '0020_logging_logdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logging',
            name='LogDate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
