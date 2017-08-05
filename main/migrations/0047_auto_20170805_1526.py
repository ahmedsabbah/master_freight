# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0046_auto_20170802_1509'),
    ]

    operations = [
        migrations.CreateModel(
            name='FCLSeaQuotation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ocean_freight', models.CharField(max_length=200, null=True, blank=True)),
                ('pre_carriage', models.CharField(max_length=200, null=True, blank=True)),
                ('thc_origin', models.CharField(max_length=200, null=True, blank=True)),
                ('custom_clearance_origin', models.CharField(max_length=200, null=True, blank=True)),
                ('documentation_origin', models.CharField(max_length=200, null=True, blank=True)),
                ('xray', models.CharField(max_length=200, null=True, blank=True)),
                ('baf', models.CharField(max_length=200, null=True, blank=True)),
                ('caf', models.CharField(max_length=200, null=True, blank=True)),
                ('others_origin', models.CharField(max_length=200, null=True, blank=True)),
                ('documentation_destination', models.CharField(max_length=200, null=True, blank=True)),
                ('thc_destination', models.CharField(max_length=200, null=True, blank=True)),
                ('storage', models.CharField(max_length=200, null=True, blank=True)),
                ('demurrage', models.CharField(max_length=200, null=True, blank=True)),
                ('custom_clearance_destination', models.CharField(max_length=200, null=True, blank=True)),
                ('road_cartage', models.CharField(max_length=200, null=True, blank=True)),
                ('on_carriage', models.CharField(max_length=200, null=True, blank=True)),
                ('others_destination', models.CharField(max_length=200, null=True, blank=True)),
                ('container_fees', models.CharField(max_length=200, null=True, blank=True)),
                ('delay', models.CharField(max_length=200, null=True, blank=True)),
                ('official_receipts_selling', models.CharField(max_length=200, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='offer',
            name='fcl_quotation',
            field=models.OneToOneField(related_name='offer', null=True, blank=True, to='main.FCLSeaQuotation'),
        ),
    ]
