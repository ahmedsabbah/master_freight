# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_auto_20170710_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='extra_information',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='reference',
            field=models.CharField(default=b'A1052C', max_length=6),
        ),
    ]
