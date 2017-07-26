# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_remove_offer_reference'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='reference',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
