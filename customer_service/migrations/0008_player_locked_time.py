# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-26 04:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_service', '0007_auto_20170925_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='locked_time',
            field=models.DateTimeField(null=True),
        ),
    ]
