# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-22 01:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='text',
        ),
        migrations.AddField(
            model_name='item',
            name='list',
            field=models.TextField(default=''),
        ),
    ]