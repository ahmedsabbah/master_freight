# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0044_auto_20170726_1559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fclcargooperations',
            name='commodity',
        ),
        migrations.RemoveField(
            model_name='fclcargooperations',
            name='container_type',
        ),
        migrations.RemoveField(
            model_name='fclcargooperations',
            name='gross_weight',
        ),
        migrations.RemoveField(
            model_name='fclcargooperations',
            name='net_weight',
        ),
        migrations.RemoveField(
            model_name='fclcargooperations',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='fclcargosales',
            name='height',
        ),
        migrations.RemoveField(
            model_name='fclcargosales',
            name='length',
        ),
        migrations.RemoveField(
            model_name='fclcargosales',
            name='total_volume',
        ),
        migrations.RemoveField(
            model_name='fclcargosales',
            name='width',
        ),
        migrations.RemoveField(
            model_name='fclquotation',
            name='bl_fees_net',
        ),
        migrations.RemoveField(
            model_name='fclquotation',
            name='clearance_pod_net',
        ),
        migrations.RemoveField(
            model_name='fclquotation',
            name='clearance_pol_net',
        ),
        migrations.RemoveField(
            model_name='fclquotation',
            name='ex_work_net',
        ),
        migrations.RemoveField(
            model_name='fclquotation',
            name='ocean_freight_net',
        ),
        migrations.RemoveField(
            model_name='fclquotation',
            name='telex_release_net',
        ),
        migrations.RemoveField(
            model_name='fclquotation',
            name='thc_net',
        ),
        migrations.RemoveField(
            model_name='fclquotation',
            name='transfer_net',
        ),
        migrations.RemoveField(
            model_name='fclquotation',
            name='transportation_net',
        ),
        migrations.AddField(
            model_name='fclquotation',
            name='baf',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fclquotation',
            name='caf',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fclquotation',
            name='container_fees',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fclquotation',
            name='custom_clearance_destination',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fclquotation',
            name='custom_clearance_origin',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fclquotation',
            name='delay',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fclquotation',
            name='demurrage',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fclquotation',
            name='documentation_destination',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fclquotation',
            name='documentation_origin',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fclquotation',
            name='ocean_freight',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fclquotation',
            name='on_carriage',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fclquotation',
            name='others_destination',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fclquotation',
            name='others_origin',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fclquotation',
            name='pre_carriage',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fclquotation',
            name='road_cartage',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fclquotation',
            name='storage',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fclquotation',
            name='thc_destination',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fclquotation',
            name='thc_origin',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fclquotation',
            name='xray',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
