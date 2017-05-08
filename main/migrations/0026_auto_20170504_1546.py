# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_auto_20170420_0233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='reference',
            field=models.CharField(default=b'486664', max_length=6),
        ),
        migrations.AlterField(
            model_name='raterequest',
            name='shipment_term',
            field=models.CharField(default='OTH', max_length=3, choices=[('EX', 'Ex-Work'), ('FAS', 'F.A.S'), ('FOB', 'F.O.B'), ('CF', 'C & F'), ('CIF', 'C.I.F'), ('OTH', 'Other')]),
        ),
        migrations.DeleteModel(
            name='ShipmentTerm',
        ),
    ]
