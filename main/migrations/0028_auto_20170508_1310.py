# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_auto_20170504_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='reference',
            field=models.CharField(default=b'554D9A', max_length=6),
        ),
    ]
