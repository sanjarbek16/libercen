# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-05 03:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_auto_20171218_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='page_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
