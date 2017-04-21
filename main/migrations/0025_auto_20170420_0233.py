# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_auto_20170420_0156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aifcargooperations',
            name='arrival_date',
        ),
        migrations.RemoveField(
            model_name='aifcargooperations',
            name='departure_date',
        ),
        migrations.AddField(
            model_name='quotation',
            name='arrival_date',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='quotation',
            name='departure_date',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='reference',
            field=models.CharField(default=b'7B101E', max_length=6),
        ),
    ]
