# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20170303_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipmentterm',
            name='title',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='reference',
            field=models.CharField(default=b'62FC94', max_length=6),
        ),
    ]
