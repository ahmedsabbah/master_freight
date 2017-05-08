# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_auto_20170504_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='client_type',
            field=models.CharField(default='IN', max_length=2, null=True, blank=True, choices=[('IN', 'Individual'), ('CO', 'Corporation or Organization'), ('BA', 'Business Address'), ('RS', 'Residence')]),
        ),
        migrations.AlterField(
            model_name='offer',
            name='reference',
            field=models.CharField(default=b'F2401F', max_length=6),
        ),
        migrations.AlterField(
            model_name='offer',
            name='status',
            field=models.CharField(default='S', max_length=2, null=True, blank=True, choices=[('S', 'Sent To Client'), ('A', 'Accepted'), ('D', 'Done'), ('R', 'Rejected')]),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='status',
            field=models.CharField(default='SS', max_length=2, null=True, blank=True, choices=[('SS', 'Sent To Sales'), ('OA', 'Offer Accepted'), ('DO', 'Done')]),
        ),
        migrations.AlterField(
            model_name='raterequest',
            name='shipment_term',
            field=models.CharField(default='OTH', max_length=3, null=True, blank=True, choices=[('EX', 'Ex-Work'), ('FAS', 'F.A.S'), ('FOB', 'F.O.B'), ('CF', 'C & F'), ('CIF', 'C.I.F'), ('OTH', 'Other')]),
        ),
        migrations.AlterField(
            model_name='raterequest',
            name='status',
            field=models.CharField(default='SO', max_length=2, null=True, blank=True, choices=[('SO', 'Sent To Operations'), ('QR', 'Quotation Received'), ('OS', 'Offer Sent'), ('OA', 'Offer Accepted'), ('DO', 'Done')]),
        ),
    ]
