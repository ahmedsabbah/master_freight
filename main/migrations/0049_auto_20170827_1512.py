# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0048_auto_20170827_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airquotation',
            name='inland',
            field=models.ForeignKey(related_name='aif_offers', blank=True, to='main.TruckerOffer', null=True),
        ),
    ]
