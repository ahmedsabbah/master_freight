# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20170305_1613'),
    ]

    operations = [
        migrations.RenameField(
            model_name='extranotes',
            old_name='vessel_available',
            new_name='vessels_available',
        ),
        migrations.AlterField(
            model_name='offer',
            name='reference',
            field=models.CharField(default=b'5ED376', max_length=6),
        ),
    ]
