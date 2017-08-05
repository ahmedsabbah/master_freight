# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0045_auto_20170726_1830'),
    ]

    operations = [
        migrations.CreateModel(
            name='Port',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TruckerOffer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('special_requirements', models.CharField(max_length=200, null=True, blank=True)),
                ('other_notes', models.CharField(max_length=200, null=True, blank=True)),
                ('price', models.CharField(max_length=200, null=True, blank=True)),
                ('port_1', models.ForeignKey(related_name='trucker_offers_port1', blank=True, to='main.Port', null=True)),
                ('port_2', models.ForeignKey(related_name='trucker_offers_port2', blank=True, to='main.Port', null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='quotation',
            name='destination',
        ),
        migrations.RemoveField(
            model_name='trucker',
            name='payment_terms',
        ),
        migrations.DeleteModel(
            name='Destination',
        ),
        migrations.AddField(
            model_name='truckeroffer',
            name='trucker',
            field=models.ForeignKey(related_name='trucker_offers', blank=True, to='main.Trucker', null=True),
        ),
    ]
