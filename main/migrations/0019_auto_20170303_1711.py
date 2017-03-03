# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20170303_1629'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trucker',
            options={'verbose_name': 'Trucker', 'verbose_name_plural': 'Truckers'},
        ),
        migrations.AlterField(
            model_name='offer',
            name='reference',
            field=models.CharField(default=b'E76C4E', max_length=6),
        ),
    ]
