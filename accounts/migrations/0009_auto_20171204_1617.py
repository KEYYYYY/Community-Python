# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20171204_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='followeds',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='followeds',
            field=models.ManyToManyField(null=True, related_name='follower', to='accounts.UserProfile', verbose_name='他关注的人'),
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='followers',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='followers',
            field=models.ManyToManyField(null=True, related_name='followed', to='accounts.UserProfile', verbose_name='关注他的人'),
        ),
    ]
