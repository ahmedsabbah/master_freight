# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_auto_20170710_1433'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aifcargosales',
            name='dimensions',
        ),
        migrations.RemoveField(
            model_name='aifcargosales',
            name='net_weight',
        ),
        migrations.RemoveField(
            model_name='fclcargosales',
            name='net_weight',
        ),
        migrations.RemoveField(
            model_name='raterequest',
            name='payment_term',
        ),
        migrations.RemoveField(
            model_name='raterequest',
            name='required_delivery_time_within',
        ),
        migrations.AddField(
            model_name='aifcargosales',
            name='chargeable_weight',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='aifcargosales',
            name='height',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='aifcargosales',
            name='length',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='aifcargosales',
            name='weight_per_piece',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='aifcargosales',
            name='width',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fclcargosales',
            name='height',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fclcargosales',
            name='length',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fclcargosales',
            name='total_volume',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fclcargosales',
            name='weight_per_piece',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fclcargosales',
            name='width',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='raterequest',
            name='airport_discharge',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='raterequest',
            name='airport_loading',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='raterequest',
            name='receipt_place',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='raterequest',
            name='shipping_terms',
            field=models.CharField(default='OTH', max_length=3, null=True, blank=True, choices=[('FILO', 'FILO'), ('FIOS', 'FIOS'), ('FIFO', 'FIFO'), ('LIFO', 'LIFO'), ('FLT', 'FLT')]),
        ),
        migrations.AlterField(
            model_name='offer',
            name='reference',
            field=models.CharField(default=b'81CCB7', max_length=6),
        ),
        migrations.AlterField(
            model_name='raterequest',
            name='shipment_term',
            field=models.CharField(default='OTH', max_length=3, null=True, blank=True, choices=[('EX', 'Ex-Work'), ('DAP', 'D.A.P'), ('DDU', 'D.D.U'), ('DDP', 'D.D.P'), ('FCA', 'F.C.A'), ('FOB', 'F.O.B'), ('CF', 'C & F'), ('CIF', 'C.I.F'), ('OTH', 'Other')]),
        ),
    ]
