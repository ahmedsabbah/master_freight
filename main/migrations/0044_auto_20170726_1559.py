# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0043_auto_20170726_1538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fclcargosales',
            name='weight_per_piece',
        ),
        migrations.AddField(
            model_name='fclcargosales',
            name='special_equipment',
            field=models.CharField(default='20RF', max_length=4, choices=[('20RF', '20 RF'), ('40RF', '40 RF'), ('20OT', '20 OT'), ('40OT', '40 OT'), ('20FR', '20 FR'), ('40FR', '40 FR')]),
        ),
        migrations.AddField(
            model_name='fclcargosales',
            name='tare_weight',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='fclcargosales',
            name='container_type',
            field=models.CharField(default='20STD', max_length=5, choices=[('20STD', '20 STD'), ('40STD', '40 STD'), ('40HC', '40 HC')]),
        ),
    ]
