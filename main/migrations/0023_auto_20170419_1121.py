# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20170305_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='reference',
            field=models.CharField(default=b'933226', max_length=6),
        ),
    ]
