# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 19:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(max_length=11, verbose_name='电话'),
        ),
    ]
