# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0040_auto_20170726_1002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seaquotation',
            name='clearance',
        ),
        migrations.RemoveField(
            model_name='seaquotation',
            name='free_time_at_destination',
        ),
        migrations.RemoveField(
            model_name='seaquotation',
            name='offer_validity',
        ),
        migrations.RemoveField(
            model_name='seaquotation',
            name='official_receipts',
        ),
        migrations.RemoveField(
            model_name='seaquotation',
            name='vessels',
        ),
        migrations.AddField(
            model_name='seaquotation',
            name='clearance_pod_selling',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='seaquotation',
            name='clearance_pol_selling',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
