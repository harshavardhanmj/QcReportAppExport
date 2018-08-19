# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-21 06:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DisStatus', '0017_auto_20180521_1042'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpcomingProj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductName', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='dailystatusauto',
            name='CurrentStatus',
            field=models.CharField(blank=True, choices=[('Scripting', 'Scripting'), ('Stability Phase', 'Stability Phase')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='dailystatuspq',
            name='CurrentStatus',
            field=models.CharField(blank=True, choices=[('IQ Script drafting', 'IQ Script drafting'), ('OQ Script drafting', 'OQ Script drafting'), ('PQ Script drafting', 'PQ Script drafting'), ('IQ Script dryrun', 'IQ Script dryrun'), ('PQ Script dryrun', 'PQ Script dryrun'), ('OQ Script dryrun', 'OQ Script dryrun'), ('IQ execution In-Progress', 'IQ execution In-Progress'), ('IQ completed', 'IQ completed'), ('OQ execution In-Progress', 'OQ execution In-Progress'), ('OQ completed', 'OQ completed'), ('PQ execution In-Progress', 'PQ execution In-Progress'), ('PQ completed', 'PQ completed')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='dailystatusqc',
            name='CurrentStatus',
            field=models.CharField(blank=True, choices=[('Test Preparation - In Progress', 'Test Preparation - In Progress'), ('Testing - In Progress', 'Testing - In Progress'), ('Testing - Completed', 'Testing - Completed')], max_length=30, null=True),
        ),
    ]