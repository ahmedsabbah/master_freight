# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_auto_20170508_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='reference',
            field=models.CharField(default=b'8FDC40', max_length=6),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='destination',
            field=models.ForeignKey(related_name='quotations', blank=True, to='main.Destination', null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='status',
            field=models.CharField(default='SS', max_length=2, null=True, blank=True, choices=[('SS', 'Sent To Sales'), ('OC', 'Offer Created'), ('OA', 'Offer Accepted'), ('OR', 'Offer Rejected'), ('DO', 'Done')]),
        ),
        migrations.AlterField(
            model_name='raterequest',
            name='status',
            field=models.CharField(default='SO', max_length=2, null=True, blank=True, choices=[('SO', 'Sent To Operations'), ('QR', 'Quotation Received'), ('OS', 'Offer Sent'), ('OA', 'Offer Accepted'), ('OR', 'Offer Rejected'), ('DO', 'Done')]),
        ),
    ]
