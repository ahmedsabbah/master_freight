# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0047_auto_20170805_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aifquotation',
            name='inland_net',
            field=models.ForeignKey(related_name='aif_quotations', blank=True, to='main.TruckerOffer', null=True),
        ),
    ]
