# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-26 15:56
from __future__ import unicode_literals

from django.db import migrations, models
import taggit_autosuggest.managers


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0018_auto_20180126_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=taggit_autosuggest.managers.TaggableManager(help_text='Select from suggestions as you type the name of the genre. If there is no genre you are looking for type comma after writing it.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Genre'),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
