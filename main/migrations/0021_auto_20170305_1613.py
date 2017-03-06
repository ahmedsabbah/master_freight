# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20170303_1746'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingline',
            old_name='any',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='raterequest',
            name='shipping_line',
        ),
        migrations.RemoveField(
            model_name='shippingline',
            name='prefered',
        ),
        migrations.AddField(
            model_name='raterequest',
            name='other_shipping_line',
            field=models.ForeignKey(related_name='other_rate_requests', blank=True, to='main.ShippingLine', null=True),
        ),
        migrations.AddField(
            model_name='raterequest',
            name='preferred_shipping_line',
            field=models.ForeignKey(related_name='rate_requests', blank=True, to='main.ShippingLine', null=True),
        ),
        migrations.AlterField(
            model_name='fclcargooperations',
            name='shipping_line',
            field=models.ForeignKey(related_name='fcl_cargos', blank=True, to='main.ShippingLine', null=True),
        ),
        migrations.AlterField(
            model_name='lclcargooperations',
            name='shipping_line',
            field=models.ForeignKey(related_name='lcl_cargos', blank=True, to='main.ShippingLine', null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='reference',
            field=models.CharField(default=b'ECE5B9', max_length=6),
        ),
        migrations.AlterField(
            model_name='offer',
            name='status',
            field=models.CharField(default='S', max_length=2, choices=[('S', 'Sent To Client'), ('A', 'Accepted'), ('D', 'Done'), ('R', 'Rejected')]),
        ),
        migrations.AlterField(
            model_name='raterequest',
            name='aif_cargo_details',
            field=models.OneToOneField(related_name='rate_requests', null=True, blank=True, to='main.AIFCargoSales'),
        ),
        migrations.AlterField(
            model_name='raterequest',
            name='destination',
            field=models.OneToOneField(related_name='rate_requests', null=True, blank=True, to='main.Destination'),
        ),
        migrations.AlterField(
            model_name='raterequest',
            name='fcl_cargo_details',
            field=models.OneToOneField(related_name='rate_requests', null=True, blank=True, to='main.FCLCargoSales'),
        ),
        migrations.AlterField(
            model_name='raterequest',
            name='lcl_cargo_details',
            field=models.OneToOneField(related_name='rate_requests', null=True, blank=True, to='main.LCLCargoSales'),
        ),
        migrations.AlterField(
            model_name='raterequest',
            name='shipment_term',
            field=models.ForeignKey(related_name='rate_requests', blank=True, to='main.ShipmentTerm', null=True),
        ),
        migrations.AlterField(
            model_name='seaquotation',
            name='shipping_line',
            field=models.ForeignKey(related_name='sea_rate_requests', blank=True, to='main.ShippingLine', null=True),
        ),
    ]
