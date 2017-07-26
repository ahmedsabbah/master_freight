# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0041_auto_20170726_1137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fclquotation',
            name='transporation_net',
        ),
        migrations.RemoveField(
            model_name='fclquotation',
            name='transporation_selling',
        ),
        migrations.RemoveField(
            model_name='lclquotation',
            name='transporation_net',
        ),
        migrations.RemoveField(
            model_name='seaquotation',
            name='transporation',
        ),
        migrations.AddField(
            model_name='fclquotation',
            name='transportation_net',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fclquotation',
            name='transportation_selling',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='lclquotation',
            name='transportation_net',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='seaquotation',
            name='transportation',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
