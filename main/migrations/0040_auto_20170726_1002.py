# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0039_auto_20170726_0315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lclcargooperations',
            name='commodity',
        ),
        migrations.RemoveField(
            model_name='lclcargooperations',
            name='dimensions_cbm',
        ),
        migrations.RemoveField(
            model_name='lclcargooperations',
            name='gross_weight',
        ),
        migrations.RemoveField(
            model_name='lclcargooperations',
            name='net_weight',
        ),
        migrations.RemoveField(
            model_name='lclquotation',
            name='bl_fees_selling',
        ),
        migrations.RemoveField(
            model_name='lclquotation',
            name='clearance_pod_selling',
        ),
        migrations.RemoveField(
            model_name='lclquotation',
            name='clearance_pol_selling',
        ),
        migrations.RemoveField(
            model_name='lclquotation',
            name='ex_work_selling',
        ),
        migrations.RemoveField(
            model_name='lclquotation',
            name='ocean_freight_selling',
        ),
        migrations.RemoveField(
            model_name='lclquotation',
            name='official_receipts_selling',
        ),
        migrations.RemoveField(
            model_name='lclquotation',
            name='telex_release_selling',
        ),
        migrations.RemoveField(
            model_name='lclquotation',
            name='thc_selling',
        ),
        migrations.RemoveField(
            model_name='lclquotation',
            name='transfer_selling',
        ),
        migrations.RemoveField(
            model_name='lclquotation',
            name='transporation_selling',
        ),
    ]
