# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0038_auto_20170725_2019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lclcargosales',
            name='net_weight',
        ),
        migrations.AddField(
            model_name='lclcargosales',
            name='height',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='lclcargosales',
            name='length',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='lclcargosales',
            name='total_volume',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='lclcargosales',
            name='weight_per_piece',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='lclcargosales',
            name='width',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
