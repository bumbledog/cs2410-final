# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-29 05:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='note_title',
            field=models.CharField(default='blank', max_length=100),
        ),
    ]