# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-27 04:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AIFCargoOperations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commodity', models.CharField(blank=True, max_length=200, null=True)),
                ('num_of_packages', models.CharField(blank=True, max_length=200, null=True)),
                ('actual_weight', models.CharField(blank=True, max_length=200, null=True)),
                ('chargeable_weight', models.CharField(blank=True, max_length=200, null=True)),
                ('dimensions', models.CharField(blank=True, max_length=200, null=True)),
                ('air_line', models.CharField(blank=True, max_length=200, null=True)),
                ('transit_time', models.CharField(blank=True, max_length=200, null=True)),
                ('route', models.CharField(blank=True, max_length=200, null=True)),
                ('departure_date', models.CharField(blank=True, max_length=200, null=True)),
                ('arrival_date', models.CharField(blank=True, max_length=200, null=True)),
                ('mawb_number', models.CharField(blank=True, max_length=200, null=True)),
                ('hawb_number', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AIFCargoSales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(blank=True, max_length=200, null=True)),
                ('commodity', models.CharField(blank=True, max_length=200, null=True)),
                ('gross_weight', models.CharField(blank=True, max_length=200, null=True)),
                ('net_weight', models.CharField(blank=True, max_length=200, null=True)),
                ('pieces', models.CharField(blank=True, max_length=200, null=True)),
                ('packing', models.CharField(blank=True, max_length=200, null=True)),
                ('dimensions', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AIFQuotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('air_freight_kg_net', models.CharField(blank=True, max_length=200, null=True)),
                ('air_freight_kg_selling', models.CharField(blank=True, max_length=200, null=True)),
                ('fuel_sur_charge_kg_net', models.CharField(blank=True, max_length=200, null=True)),
                ('fuel_sur_charge_kg_selling', models.CharField(blank=True, max_length=200, null=True)),
                ('security_fees_kg_net', models.CharField(blank=True, max_length=200, null=True)),
                ('security_fees_kg_selling', models.CharField(blank=True, max_length=200, null=True)),
                ('exw_charges_net', models.CharField(blank=True, max_length=200, null=True)),
                ('exw_charges_selling', models.CharField(blank=True, max_length=200, null=True)),
                ('screening_fees_net', models.CharField(blank=True, max_length=200, null=True)),
                ('screening_fees_selling', models.CharField(blank=True, max_length=200, null=True)),
                ('storage_net', models.CharField(blank=True, max_length=200, null=True)),
                ('storage_selling', models.CharField(blank=True, max_length=200, null=True)),
                ('inland_net', models.CharField(blank=True, max_length=200, null=True)),
                ('inland_selling', models.CharField(blank=True, max_length=200, null=True)),
                ('packing_net', models.CharField(blank=True, max_length=200, null=True)),
                ('packing_selling', models.CharField(blank=True, max_length=200, null=True)),
                ('taxes_duties_net', models.CharField(blank=True, max_length=200, null=True)),
                ('taxes_duties_selling', models.CharField(blank=True, max_length=200, null=True)),
                ('handling_fees_net', models.CharField(blank=True, max_length=200, null=True)),
                ('handling_fees_selling', models.CharField(blank=True, max_length=200, null=True)),
                ('p_share_net', models.CharField(blank=True, max_length=200, null=True)),
                ('p_share_selling', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('company_name', models.CharField(blank=True, max_length=200, null=True)),
                ('contact', models.TextField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_information', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port_of_loading', models.CharField(blank=True, max_length=200, null=True)),
                ('loading_location_type', models.CharField(blank=True, max_length=200, null=True)),
                ('port_of_discharge', models.CharField(blank=True, max_length=200, null=True)),
                ('discharge_location_type', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExtraNotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('free_time_at_destination', models.CharField(blank=True, max_length=200, null=True)),
                ('vessel_available', models.CharField(blank=True, max_length=200, null=True)),
                ('route', models.CharField(blank=True, max_length=200, null=True)),
                ('transit_time', models.CharField(blank=True, max_length=200, null=True)),
                ('offer_validity', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FCLCargoOperations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipping_line', models.CharField(blank=True, max_length=200, null=True)),
                ('container_type', models.CharField(blank=True, max_length=200, null=True)),
                ('quantity', models.CharField(blank=True, max_length=200, null=True)),
                ('commodity', models.CharField(blank=True, max_length=200, null=True)),
                ('gross_weight', models.CharField(blank=True, max_length=200, null=True)),
                ('net_weight', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FCLCargoSales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('container_type', models.CharField(blank=True, max_length=200, null=True)),
                ('quantity', models.CharField(blank=True, max_length=200, null=True)),
                ('commodity', models.CharField(blank=True, max_length=200, null=True)),
                ('gross_weight', models.CharField(blank=True, max_length=200, null=True)),
                ('net_weight', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FCLQuotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ocean_freight_net', models.CharField(blank=True, max_length=200, null=True)),
                ('ocean_freight_selling', models.CharField(blank=True, max_length=200, null=True)),
                ('thc_net', models.CharField(blank=True, max_length=200, null=True)),
                ('thc_selling', models.CharField(blank=True, max_length=200, null=True)),
                ('transporation_net', models.CharField(blank=True, max_length=200, null=True)),
                ('transporation_selling', models.CharField(blank=True, max_length=200, null=True)),
                ('transfer_net', models.CharField(blank=True, max_length=200, null=True)),
                ('transfer_selling', models.CharField(blank=True, max_length=200, null=True)),
                ('clearance_pol_net', models.CharField(blank=True, max_length=200, null=True)),
                ('clearance_pol_selling', models.CharField(blank=True, max_length=200, null=True)),
                ('clearance_pod_net', models.CharField(blank=True, max_length=200, null=True)),
                ('clearance_pod_selling', models.CharField(blank=True, max_length=200, null=True)),
                ('bl_fees_net', models.CharField(blank=True, max_length=200, null=True)),
                ('bl_fees_selling', models.CharField(blank=True, max_length=200, null=True)),
                ('telex_release_net', models.CharField(blank=True, max_length=200, null=True)),
                ('telex_release_selling', models.CharField(blank=True, max_length=200, null=True)),
                ('ex_work_net', models.CharField(blank=True, max_length=200, null=True)),
                ('ex_work_selling', models.CharField(blank=True, max_length=200, null=True)),
                ('official_receipts_net', models.CharField(blank=True, max_length=200, null=True)),
                ('official_receipts_selling', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FinalDeliveryDestination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('contact_person', models.CharField(blank=True, max_length=200, null=True)),
                ('contact_person_extra', models.TextField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IMOClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hazardous', models.CharField(blank=True, max_length=200, null=True)),
                ('non_hazardous', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LCLCargoOperations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipping_line', models.CharField(blank=True, max_length=200, null=True)),
                ('container_type', models.CharField(blank=True, max_length=200, null=True)),
                ('num_of_packages', models.CharField(blank=True, max_length=200, null=True)),
                ('commodity', models.CharField(blank=True, max_length=200, null=True)),
                ('gross_weight', models.CharField(blank=True, max_length=200, null=True)),
                ('net_weight', models.CharField(blank=True, max_length=200, null=True)),
                ('dimensions_cbm', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LCLCargoSales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(blank=True, max_length=200, null=True)),
                ('commodity', models.CharField(blank=True, max_length=200, null=True)),
                ('gross_weight', models.CharField(blank=True, max_length=200, null=True)),
                ('net_weight', models.CharField(blank=True, max_length=200, null=True)),
                ('pieces', models.CharField(blank=True, max_length=200, null=True)),
                ('packing', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LCLQuotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ocean_freight_net', models.CharField(blank=True, max_length=200, null=True)),
                ('ocean_freight_selling', models.CharField(blank=True, max_length=200, null=True)),
                ('thc_net', models.CharField(blank=True, max_length=200, null=True)),
                ('thc_selling', models.CharField(blank=True, max_length=200, null=True)),
                ('transporation_net', models.CharField(blank=True, max_length=200, null=True)),
                ('transporation_selling', models.CharField(blank=True, max_length=200, null=True)),
                ('transfer_net', models.CharField(blank=True, max_length=200, null=True)),
                ('transfer_selling', models.CharField(blank=True, max_length=200, null=True)),
                ('clearance_pol_net', models.CharField(blank=True, max_length=200, null=True)),
                ('clearance_pol_selling', models.CharField(blank=True, max_length=200, null=True)),
                ('clearance_pod_net', models.CharField(blank=True, max_length=200, null=True)),
                ('clearance_pod_selling', models.CharField(blank=True, max_length=200, null=True)),
                ('bl_fees_net', models.CharField(blank=True, max_length=200, null=True)),
                ('bl_fees_selling', models.CharField(blank=True, max_length=200, null=True)),
                ('telex_release_net', models.CharField(blank=True, max_length=200, null=True)),
                ('telex_release_selling', models.CharField(blank=True, max_length=200, null=True)),
                ('ex_work_net', models.CharField(blank=True, max_length=200, null=True)),
                ('ex_work_selling', models.CharField(blank=True, max_length=200, null=True)),
                ('official_receipts_net', models.CharField(blank=True, max_length=200, null=True)),
                ('official_receipts_selling', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('AIF', 'AIF'), ('FCL', 'FCL'), ('LCL', 'LCL')], max_length=3)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('agent_details', models.CharField(blank=True, max_length=200, null=True)),
                ('co_loader', models.CharField(blank=True, max_length=200, null=True)),
                ('special_instructions', models.TextField(blank=True, null=True)),
                ('aif_cargo_details', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quotation', to='main.AIFCargoOperations')),
                ('aif_quotation', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quotation', to='main.AIFQuotation')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quotations', to='main.Client')),
                ('destination', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quotation', to='main.Destination')),
                ('extra_notes', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quotation', to='main.ExtraNotes')),
                ('fcl_cargo_details', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quotation', to='main.FCLCargoOperations')),
                ('fcl_quotation', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quotation', to='main.FCLQuotation')),
                ('lcl_cargo_details', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quotation', to='main.LCLCargoOperations')),
                ('lcl_quotation', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quotation', to='main.LCLQuotation')),
                ('operations_person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quotations', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Quotation',
                'verbose_name_plural': 'Quotations',
            },
        ),
        migrations.CreateModel(
            name='RateRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('AIF', 'AIF'), ('FCL', 'FCL'), ('LCL', 'LCL')], max_length=3)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('required_delivery_time_within', models.CharField(blank=True, max_length=200, null=True)),
                ('payment_term', models.CharField(blank=True, max_length=200, null=True)),
                ('special_instructions', models.TextField(blank=True, null=True)),
                ('aif_cargo_details', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rate_request', to='main.AIFCargoSales')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rate_requests', to='main.Client')),
                ('destination', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rate_request', to='main.Destination')),
                ('fcl_cargo_details', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rate_request', to='main.FCLCargoSales')),
                ('final_delivery_destination', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rate_request', to='main.FinalDeliveryDestination')),
                ('imo_class', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rate_request', to='main.IMOClass')),
                ('lcl_cargo_details', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rate_request', to='main.LCLCargoSales')),
                ('sales_person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rate_requests', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Rate Request',
                'verbose_name_plural': 'Rate Requests',
            },
        ),
        migrations.CreateModel(
            name='ShipmentTerm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ex_work', models.CharField(blank=True, max_length=200, null=True)),
                ('fas', models.CharField(blank=True, max_length=200, null=True)),
                ('fob', models.CharField(blank=True, max_length=200, null=True)),
                ('cf', models.CharField(blank=True, max_length=200, null=True)),
                ('cif', models.CharField(blank=True, max_length=200, null=True)),
                ('others', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefered', models.CharField(blank=True, max_length=200, null=True)),
                ('any', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='raterequest',
            name='shipment_term',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rate_request', to='main.ShipmentTerm'),
        ),
        migrations.AddField(
            model_name='raterequest',
            name='shipping_line',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rate_request', to='main.ShippingLine'),
        ),
    ]
