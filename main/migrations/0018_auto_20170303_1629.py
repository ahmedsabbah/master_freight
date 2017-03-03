# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20170226_2129'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trucker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company_name', models.CharField(max_length=200, null=True, blank=True)),
                ('address', models.CharField(max_length=200, null=True, blank=True)),
                ('op_name', models.CharField(max_length=200, null=True, blank=True)),
                ('op_phone', models.CharField(max_length=200, null=True, blank=True)),
                ('op_email', models.CharField(max_length=200, null=True, blank=True)),
                ('acc_name', models.CharField(max_length=200, null=True, blank=True)),
                ('acc_phone', models.CharField(max_length=200, null=True, blank=True)),
                ('acc_email', models.CharField(max_length=200, null=True, blank=True)),
                ('payment_terms', models.CharField(max_length=200, null=True, blank=True)),
                ('special_requirements', models.CharField(max_length=200, null=True, blank=True)),
                ('other_notes', models.CharField(max_length=200, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='company_name',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='airquotation',
            name='inland',
            field=models.ForeignKey(related_name='quotations', blank=True, to='main.Trucker', null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='reference',
            field=models.CharField(default=b'0915C5', max_length=6),
        ),
    ]
