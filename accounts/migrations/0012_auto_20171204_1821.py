# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 18:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20171204_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='followers',
            field=models.ManyToManyField(related_name='followeds', to='accounts.UserProfile', verbose_name='关注他的人'),
        ),
    ]
