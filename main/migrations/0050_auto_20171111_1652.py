# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0049_auto_20170827_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotation',
            name='aif_quotation',
            field=models.OneToOneField(related_name='aif_quotation', null=True, blank=True, to='main.AIFQuotation'),
        ),
    ]
