# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_auto_20170725_1848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aifcargooperations',
            name='air_line',
        ),
        migrations.RemoveField(
            model_name='aifcargooperations',
            name='chargeable_weight',
        ),
        migrations.RemoveField(
            model_name='aifcargooperations',
            name='commodity',
        ),
        migrations.RemoveField(
            model_name='aifcargooperations',
            name='dimensions',
        ),
        migrations.RemoveField(
            model_name='aifquotation',
            name='air_freight_kg_selling',
        ),
        migrations.RemoveField(
            model_name='aifquotation',
            name='exw_charges_selling',
        ),
        migrations.RemoveField(
            model_name='aifquotation',
            name='fuel_sur_charge_kg_selling',
        ),
        migrations.RemoveField(
            model_name='aifquotation',
            name='handling_fees_selling',
        ),
        migrations.RemoveField(
            model_name='aifquotation',
            name='inland_selling',
        ),
        migrations.RemoveField(
            model_name='aifquotation',
            name='p_share_selling',
        ),
        migrations.RemoveField(
            model_name='aifquotation',
            name='packing_selling',
        ),
        migrations.RemoveField(
            model_name='aifquotation',
            name='screening_fees_selling',
        ),
        migrations.RemoveField(
            model_name='aifquotation',
            name='security_fees_kg_selling',
        ),
        migrations.RemoveField(
            model_name='aifquotation',
            name='storage_selling',
        ),
        migrations.RemoveField(
            model_name='aifquotation',
            name='taxes_duties_selling',
        ),
        migrations.AlterField(
            model_name='offer',
            name='reference',
            field=models.UUIDField(default=uuid.uuid4, unique=False, editable=False),
        ),
    ]
