# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-09 13:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DisStatus', '0012_auto_20180509_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailystatusqc',
            name='PlanEndDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dailystatusqc',
            name='PlanStartDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
