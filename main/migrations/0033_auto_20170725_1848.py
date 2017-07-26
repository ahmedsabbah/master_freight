# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_auto_20170725_1829'),
    ]

    operations = [
        migrations.RenameField(
            model_name='raterequest',
            old_name='airport_discharge',
            new_name='port_discharge',
        ),
        migrations.RenameField(
            model_name='raterequest',
            old_name='airport_loading',
            new_name='port_loading',
        ),
        migrations.RemoveField(
            model_name='raterequest',
            name='destination',
        ),
        migrations.AlterField(
            model_name='offer',
            name='reference',
            field=models.CharField(default=b'EC9F5B', max_length=6),
        ),
    ]
