# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0035_auto_20170725_2003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='reference',
        ),
    ]
