# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20170226_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='quotation',
            field=models.ForeignKey(related_name='offers', to='main.Quotation'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='reference',
            field=models.CharField(default=b'06AEE3', max_length=6),
        ),
    ]
