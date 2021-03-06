# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-18 06:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DisStatus', '0025_auto_20180522_1212'),
    ]

    operations = [
        migrations.CreateModel(
            name='graphData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectName', models.CharField(blank=True, max_length=100, null=True)),
                ('plotDate', models.CharField(blank=True, max_length=100, null=True)),
                ('issueLogged', models.CharField(blank=True, max_length=100, null=True)),
                ('issueClosed', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='dailystatuspq',
            name='CurrentStatus',
            field=models.CharField(blank=True, choices=[('IQ,OQ,PQ Script drafting', 'IQ,OQ,PQ Script drafting'), ('IQ,OQ,PQ Script dryrun', 'IQ,OQ,PQ Script dryrun'), ('IQ execution In-Progress', 'IQ execution In-Progress'), ('IQ completed', 'IQ completed'), ('OQ execution In-Progress', 'OQ execution In-Progress'), ('OQ completed', 'OQ completed'), ('PQ execution In-Progress', 'PQ execution In-Progress'), ('PQ completed', 'PQ completed')], max_length=100, null=True),
        ),
    ]
