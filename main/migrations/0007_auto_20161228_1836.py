# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-12-28 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20161208_0455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='reference',
            field=models.CharField(default=b'AAD9D4', max_length=6),
        ),
    ]
