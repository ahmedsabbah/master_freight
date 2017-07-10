# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_auto_20170705_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='terms',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='reference',
            field=models.CharField(default=b'06BD6F', max_length=6),
        ),
    ]
