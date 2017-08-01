# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0042_auto_20170726_1414'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fclquotation',
            name='bl_fees_selling',
        ),
        migrations.RemoveField(
            model_name='fclquotation',
            name='clearance_pod_selling',
        ),
        migrations.RemoveField(
            model_name='fclquotation',
            name='clearance_pol_selling',
        ),
        migrations.RemoveField(
            model_name='fclquotation',
            name='ex_work_selling',
        ),
        migrations.RemoveField(
            model_name='fclquotation',
            name='ocean_freight_selling',
        ),
        migrations.RemoveField(
            model_name='fclquotation',
            name='official_receipts_selling',
        ),
        migrations.RemoveField(
            model_name='fclquotation',
            name='telex_release_selling',
        ),
        migrations.RemoveField(
            model_name='fclquotation',
            name='thc_selling',
        ),
        migrations.RemoveField(
            model_name='fclquotation',
            name='transfer_selling',
        ),
        migrations.RemoveField(
            model_name='fclquotation',
            name='transportation_selling',
        ),
        migrations.AlterField(
            model_name='quotation',
            name='type',
            field=models.CharField(max_length=4, choices=[('AIF', 'AIF'), ('IFCL', 'FCL IMPORT'), ('XFCL', 'FCL EXPORT'), ('LCL', 'LCL')]),
        ),
        migrations.AlterField(
            model_name='raterequest',
            name='type',
            field=models.CharField(max_length=4, choices=[('AIF', 'AIF'), ('IFCL', 'FCL IMPORT'), ('XFCL', 'FCL EXPORT'), ('LCL', 'LCL')]),
        ),
    ]
