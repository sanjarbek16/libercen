# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-06 01:12
from __future__ import unicode_literals

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_fav_books'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=users.models.upload_to),
        ),
        migrations.AlterField(
            model_name='profile',
            name='back_image',
            field=models.ImageField(blank=True, null=True, upload_to=users.models.upload_back),
        ),
    ]
