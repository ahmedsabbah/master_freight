# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20170419_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotation',
            name='current_location',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='reference',
            field=models.CharField(default=b'DE4BBC', max_length=6),
        ),
    ]
