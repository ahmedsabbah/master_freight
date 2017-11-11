# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0050_auto_20171111_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airquotation',
            name='inland',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
