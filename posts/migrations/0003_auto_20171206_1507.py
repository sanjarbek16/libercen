# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-06 15:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_users_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='users_like',
            field=models.ManyToManyField(blank=True, related_name='posts_liked', to=settings.AUTH_USER_MODEL),
        ),
    ]
