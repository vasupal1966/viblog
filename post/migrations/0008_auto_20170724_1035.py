# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-24 10:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_auto_20170708_1358'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
    ]
