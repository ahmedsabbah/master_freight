from __future__ import unicode_literals
from django.db import models
import uuid

class Todo(models.Model):
    user = models.ForeignKey('authentication.User', related_name='todos')
    text = models.CharField(max_length=400)
    created_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'
    def _str__(self):
        return self.text

class Client(models.Model):
    TYPE_CHOICES = (
        ('IN', 'Individual'),
        ('CO', 'Corporation or Organization'),
        ('BA', 'Business Address'),
        ('RS', 'Residence'),
    )

    client_name = models.CharField(max_length=200, blank=True, null=True)
    company_name = models.CharField(max_length=200, blank=True, null=True)
    client_type = models.CharField(max_length=2, choices=TYPE_CHOICES, default='IN', null=True, blank=True)
    client_address = models.CharField(max_length=200, blank=True, null=True)
    commodity = models.CharField(max_length=200, blank=True, null=True)
    business_phone = models.CharField(max_length=100, blank=True, null=True)
    alt_phone = models.CharField(max_length=100, blank=True, null=True)
    fax = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=False, unique=True, null=True)
    op_contact = models.CharField(max_length=200, blank=True, null=True)
    op_job_title = models.CharField(max_length=200, blank=True, null=True)
    op_business_phone = models.CharField(max_length=200, blank=True, null=True)
    op_email = models.CharField(max_length=200, blank=True, null=True)
    op_phone = models.CharField(max_length=200, blank=True, null=True)
    finance_contact = models.CharField(max_length=200, blank=True, null=True)
    finance_job_title = models.CharField(max_length=200, blank=True, null=True)
    finance_business_phone = models.CharField(max_length=200, blank=True, null=True)
    finance_email = models.CharField(max_length=200, blank=True, null=True)
    finance_phone = models.CharField(max_length=200, blank=True, null=True)
    client_id_number = models.CharField(max_length=100, blank=True, null=True)
    credit_period = models.CharField(max_length=100, blank=True, null=True)
    credit_limit = models.CharField(max_length=100, blank=True, null=True)
    reference_name = models.CharField(max_length=100, blank=True, null=True)
    reference_phone = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField(max_length=250, blank=True, null=True)
    issued_by = models.CharField(max_length=100, blank=True, null=True)
    authorized_by = models.CharField(max_length=100, blank=True, null=True)
    extra_information = models.CharField(max_length=300, blank=True, null=True)
    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
    def __str__(self):
        return self.client_name
class Trucker(models.Model):
    company_name = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    op_name = models.CharField(max_length=200, blank=True, null=True)
    op_phone = models.CharField(max_length=200, blank=True, null=True)
    op_email = models.CharField(max_length=200, blank=True, null=True)
    acc_name = models.CharField(max_length=200, blank=True, null=True)
    acc_phone = models.CharField(max_length=200, blank=True, null=True)
    acc_email = models.CharField(max_length=200, blank=True, null=True)
    special_requirements = models.CharField(max_length=200, blank=True, null=True)
    other_notes = models.CharField(max_length=200, blank=True, null=True)
    class Meta:
        verbose_name = 'Trucker'
        verbose_name_plural = 'Truckers'
    def __str__(self):
        return str(self.company_name)

class Port(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return str(self.name)

class TruckerOffer(models.Model):
    port_1 = models.ForeignKey('Port', related_name='trucker_offers_port1', blank=True, null=True)
    port_2 = models.ForeignKey('Port', related_name='trucker_offers_port2', blank=True, null=True)
    trucker = models.ForeignKey('Trucker', related_name='trucker_offers', blank=True, null=True)
    special_requirements = models.CharField(max_length=200, blank=True, null=True)
    other_notes = models.CharField(max_length=200, blank=True, null=True)
    price = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return 'from %s to %s with %s - %s' % (self.port_1, self.port_2, self.trucker, self.price)


class FinalDeliveryDestination(models.Model):
    address = models.CharField(max_length=200, blank=True, null=True)
    contact_person = models.CharField(max_length=200, blank=True, null=True)
    contact_person_extra = models.TextField(max_length=200, blank=True, null=True)

class AIFCargoSales(models.Model):
    quantity = models.CharField(max_length=200, blank=True, null=True)
    commodity = models.CharField(max_length=200, blank=True, null=True)
    gross_weight = models.CharField(max_length=200, blank=True, null=True)
    weight_per_piece = models.CharField(max_length=200, blank=True, null=True)
    length = models.CharField(max_length=200, blank=True, null=True)
    width = models.CharField(max_length=200, blank=True, null=True)
    height = models.CharField(max_length=200, blank=True, null=True)
    chargeable_weight = models.CharField(max_length=200, blank=True, null=True)
    pieces = models.CharField(max_length=200, blank=True, null=True)
    packing = models.CharField(max_length=200, blank=True, null=True)

class FCLCargoSales(models.Model):
    CONTAINER_TYPE_CHOICES = (
        ('20STD', '20 STD'),
        ('40STD', '40 STD'),
        ('40HC', '40 HC'),
    )
    EQUIPMENT_TYPE_CHOICES = (
        ('20RF', '20 RF'),
        ('40RF', '40 RF'),
        ('20OT', '20 OT'),
        ('40OT', '40 OT'),
        ('20FR', '20 FR'),
        ('40FR', '40 FR'),
    )
    container_type = models.CharField(max_length=5, default="20STD", choices=CONTAINER_TYPE_CHOICES)
    special_equipment = models.CharField(max_length=4, default="20RF", choices=EQUIPMENT_TYPE_CHOICES)
    quantity = models.CharField(max_length=200, blank=True, null=True)
    commodity = models.CharField(max_length=200, blank=True, null=True)
    gross_weight = models.CharField(max_length=200, blank=True, null=True)
    tare_weight = models.CharField(max_length=200, blank=True, null=True)

class LCLCargoSales(models.Model):
    quantity = models.CharField(max_length=200, blank=True, null=True)
    commodity = models.CharField(max_length=200, blank=True, null=True)
    gross_weight = models.CharField(max_length=200, blank=True, null=True)
    weight_per_piece = models.CharField(max_length=200, blank=True, null=True)
    length = models.CharField(max_length=200, blank=True, null=True)
    width = models.CharField(max_length=200, blank=True, null=True)
    height = models.CharField(max_length=200, blank=True, null=True)
    total_volume = models.CharField(max_length=200, blank=True, null=True)
    pieces = models.CharField(max_length=200, blank=True, null=True)
    packing = models.CharField(max_length=200, blank=True, null=True)

class ShippingLine(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return self.name

class IMOClass(models.Model):
    hazardous = models.CharField(max_length=200, blank=True, null=True)
    non_hazardous = models.CharField(max_length=200, blank=True, null=True)

class RateRequest(models.Model):
    TYPE_CHOICES = (
        ('AIF', 'AIF'),
        ('IFCL', 'FCL IMPORT'),
        ('XFCL', 'FCL EXPORT'),
        ('LCL', 'LCL')
    )
    STATUS_CHOICES = (
        ('SO', 'Sent To Operations'),
        ('QR', 'Quotation Received'),
        ('OS', 'Offer Sent'),
        ('OA', 'Offer Accepted'),
        ('OR', 'Offer Rejected'),
        ('DO', 'Done')
    )
    SHIPMENT_TERM_CHOICES = (
        ('EX','Ex-Work'),
        ('DAP', 'D.A.P'),
        ('DDU', 'D.D.U'),
        ('DDP', 'D.D.P'),
        ('FCA', 'F.C.A'),
        ('FOB', 'F.O.B'),
        ('CF', 'C & F'),
        ('CIF', 'C.I.F'),
        ('OTH', 'Other')
    )
    SHIPPING_TERMS_CHOICES = (
        ('FILO','FILO'),
        ('FIOS', 'FIOS'),
        ('FIFO', 'FIFO'),
        ('LIFO', 'LIFO'),
        ('FLT', 'FLT'),
    )
    type = models.CharField(max_length=4, choices=TYPE_CHOICES)
    created_date = models.DateTimeField(auto_now_add=True)
    sales_person = models.ForeignKey('authentication.User', related_name='rate_requests', blank=True, null=True)
    client = models.ForeignKey('main.Client', related_name='rate_requests', blank=True, null=True)
    # destination = models.OneToOneField('main.Destination', related_name='rate_requests', blank=True, null=True)
    final_delivery_destination = models.OneToOneField('main.FinalDeliveryDestination', related_name='rate_request', blank=True, null=True)
    receipt_place = models.CharField(max_length=200, blank=True, null=True)
    port_discharge = models.CharField(max_length=200, blank=True, null=True)
    port_loading = models.CharField(max_length=200, blank=True, null=True)
    aif_cargo_details = models.OneToOneField('main.AIFCargoSales', related_name='rate_requests', blank=True, null=True)
    fcl_cargo_details = models.OneToOneField('main.FCLCargoSales', related_name='rate_requests', blank=True, null=True)
    lcl_cargo_details = models.OneToOneField('main.LCLCargoSales', related_name='rate_requests', blank=True, null=True)
    preferred_shipping_line = models.ForeignKey('main.ShippingLine', related_name='rate_requests', null=True, blank=True)
    other_shipping_line = models.ForeignKey('main.ShippingLine', related_name='other_rate_requests', null=True, blank=True)
    imo_class = models.OneToOneField('main.IMOClass', related_name='rate_request', blank=True, null=True)
    shipment_term =  models.CharField(max_length=3, choices=SHIPMENT_TERM_CHOICES, default='OTH', null=True, blank=True)
    shipping_terms =  models.CharField(max_length=3, choices=SHIPPING_TERMS_CHOICES, default='OTH', null=True, blank=True)
    special_instructions = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='SO', null=True, blank=True)
    class Meta:
        verbose_name = 'Rate Request'
        verbose_name_plural = 'Rate Requests'
    def __str__(self):
        return self.client.client_name
    def status_verbose(self):
        return dict(RateRequest.STATUS_CHOCIES)[self.status]

class AIFCargoOperations(models.Model):
    num_of_packages = models.CharField(max_length=200, blank=True, null=True)
    actual_weight = models.CharField(max_length=200, blank=True, null=True)
    transit_time = models.CharField(max_length=200, blank=True, null=True)
    route = models.CharField(max_length=200, blank=True, null=True)
    mawb_number = models.CharField(max_length=200, blank=True, null=True)
    hawb_number = models.CharField(max_length=200, blank=True, null=True)

class FCLCargoOperations(models.Model):

    shipping_line = models.ForeignKey('main.ShippingLine', related_name='fcl_cargos', null=True, blank=True)

class LCLCargoOperations(models.Model):
    shipping_line = models.ForeignKey('main.ShippingLine', related_name='lcl_cargos', null=True, blank=True)
    container_type = models.CharField(max_length=200, blank=True, null=True)
    num_of_packages = models.CharField(max_length=200, blank=True, null=True)

class AIFQuotation(models.Model):
    air_freight_kg_net = models.CharField(max_length=200, blank=True, null=True)
    fuel_sur_charge_kg_net = models.CharField(max_length=200, blank=True, null=True)
    security_fees_kg_net = models.CharField(max_length=200, blank=True, null=True)
    exw_charges_net = models.CharField(max_length=200, blank=True, null=True)
    screening_fees_net = models.CharField(max_length=200, blank=True, null=True)
    storage_net = models.CharField(max_length=200, blank=True, null=True)
    inland_net = models.ForeignKey('main.TruckerOffer', related_name='aif_quotations', null=True, blank=True)
    packing_net = models.CharField(max_length=200, blank=True, null=True)
    taxes_duties_net = models.CharField(max_length=200, blank=True, null=True)
    handling_fees_net = models.CharField(max_length=200, blank=True, null=True)
    p_share_net = models.CharField(max_length=200, blank=True, null=True)

class FCLQuotation(models.Model):
    ocean_freight = models.CharField(max_length=200, blank=True, null=True)
    pre_carriage = models.CharField(max_length=200, blank=True, null=True)
    thc_origin = models.CharField(max_length=200, blank=True, null=True)
    custom_clearance_origin = models.CharField(max_length=200, blank=True, null=True)
    documentation_origin = models.CharField(max_length=200, blank=True, null=True)
    xray = models.CharField(max_length=200, blank=True, null=True)
    baf = models.CharField(max_length=200, blank=True, null=True)
    caf = models.CharField(max_length=200, blank=True, null=True)
    others_origin = models.CharField(max_length=200, blank=True, null=True)
    documentation_destination = models.CharField(max_length=200, blank=True, null=True)
    thc_destination = models.CharField(max_length=200, blank=True, null=True)
    storage = models.CharField(max_length=200, blank=True, null=True)
    demurrage = models.CharField(max_length=200, blank=True, null=True)
    custom_clearance_destination = models.CharField(max_length=200, blank=True, null=True)
    road_cartage = models.CharField(max_length=200, blank=True, null=True)
    on_carriage = models.CharField(max_length=200, blank=True, null=True)
    others_destination = models.CharField(max_length=200, blank=True, null=True)
    container_fees = models.CharField(max_length=200, blank=True, null=True)
    delay = models.CharField(max_length=200, blank=True, null=True)
    official_receipts_net = models.CharField(max_length=200, blank=True, null=True)

class LCLQuotation(models.Model):
    ocean_freight_net = models.CharField(max_length=200, blank=True, null=True)
    thc_net = models.CharField(max_length=200, blank=True, null=True)
    transportation_net = models.CharField(max_length=200, blank=True, null=True)
    transfer_net = models.CharField(max_length=200, blank=True, null=True)
    clearance_pol_net = models.CharField(max_length=200, blank=True, null=True)
    clearance_pod_net = models.CharField(max_length=200, blank=True, null=True)
    bl_fees_net = models.CharField(max_length=200, blank=True, null=True)
    telex_release_net = models.CharField(max_length=200, blank=True, null=True)
    ex_work_net = models.CharField(max_length=200, blank=True, null=True)
    official_receipts_net = models.CharField(max_length=200, blank=True, null=True)

class ExtraNotes(models.Model):
    free_time_at_destination = models.CharField(max_length=200, blank=True, null=True)
    vessels_available = models.CharField(max_length=200, blank=True, null=True)
    route = models.CharField(max_length=200, blank=True, null=True)
    transit_time = models.CharField(max_length=200, blank=True, null=True)
    offer_validity = models.CharField(max_length=200, blank=True, null=True)

class Quotation(models.Model):
    TYPE_CHOICES = (
        ('AIF', 'AIF'),
        ('IFCL', 'FCL IMPORT'),
        ('XFCL', 'FCL EXPORT'),
        ('LCL', 'LCL')
    )
    STATUS_CHOICES = (
        ('SS', 'Sent To Sales'),
        ('OC', 'Offer Created'),
        ('OA', 'Offer Accepted'),
        ('OR', 'Offer Rejected'),
        ('DO', 'Done')
    )
    rate_request = models.ForeignKey('main.RateRequest', related_name='quotations', blank=True, null=True)
    type = models.CharField(max_length=4, choices=TYPE_CHOICES)
    current_location = models.CharField(max_length=200, null=True, blank=True)
    departure_date = models.CharField(max_length=200, blank=True, null=True)
    arrival_date = models.CharField(max_length=200, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    sales_person = models.ForeignKey('authentication.User', related_name='quotations_sales', blank=True, null=True)
    operations_person = models.ForeignKey('authentication.User', related_name='quotations_operations', blank=True, null=True)
    client = models.ForeignKey('main.Client', related_name='quotations', blank=True, null=True)
    agent_details = models.CharField(max_length=200, blank=True, null=True)
    co_loader = models.CharField(max_length=200, blank=True, null=True)
    aif_cargo_details = models.OneToOneField('main.AIFCargoOperations', related_name='quotation', blank=True, null=True)
    fcl_cargo_details = models.OneToOneField('main.FCLCargoOperations', related_name='quotation', blank=True, null=True)
    lcl_cargo_details = models.OneToOneField('main.LCLCargoOperations', related_name='quotation', blank=True, null=True)
    aif_quotation = models.OneToOneField('main.AIFQuotation', related_name='aif_quotation', blank=True, null=True)
    fcl_quotation = models.OneToOneField('main.FCLQuotation', related_name='quotation', blank=True, null=True)
    lcl_quotation = models.OneToOneField('main.LCLQuotation', related_name='quotation', blank=True, null=True)
    extra_notes = models.OneToOneField('main.ExtraNotes', related_name='quotation', blank=True, null=True)
    special_instructions = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='SS', null=True, blank=True)
    class Meta:
        verbose_name = 'Quotation'
        verbose_name_plural = 'Quotations'
    def __str__(self):
        return self.client.client_name

    def status_verbose(self):
        return dict(Quotation.STATUS_CHOCIES)[self.status]

class AirQuotation(models.Model):
    air_freight_kg = models.CharField(max_length=200, blank=True, null=True)
    fuel_sur_charge_kg = models.CharField(max_length=200, blank=True, null=True)
    security_fees_kg = models.CharField(max_length=200, blank=True, null=True)
    exw_charges = models.CharField(max_length=200, blank=True, null=True)
    screening_fees = models.CharField(max_length=200, blank=True, null=True)
    storage = models.CharField(max_length=200, blank=True, null=True)
    inland = models.CharField(max_length=200, null=True, blank=True)
    packing = models.CharField(max_length=200, blank=True, null=True)
    taxes_duties = models.CharField(max_length=200, blank=True, null=True)
    handling_fees = models.CharField(max_length=200, blank=True, null=True)
    official_receipts = models.CharField(max_length=200, blank=True, null=True)
    p_share = models.CharField(max_length=200, blank=True, null=True)
    other_notes = models.CharField(max_length=200, blank=True, null=True)
    offer_validity = models.CharField(max_length=200, blank=True, null=True)

class SeaQuotation(models.Model):
    shipping_line = models.ForeignKey('main.ShippingLine', related_name='sea_rate_requests', null=True, blank=True)
    ocean_freight = models.CharField(max_length=200, blank=True, null=True)
    thc = models.CharField(max_length=200, blank=True, null=True)
    transportation = models.CharField(max_length=200, blank=True, null=True)
    transfer = models.CharField(max_length=200, blank=True, null=True)
    clearance_pol_selling = models.CharField(max_length=200, blank=True, null=True)
    clearance_pod_selling = models.CharField(max_length=200, blank=True, null=True)
    bl_fees = models.CharField(max_length=200, blank=True, null=True)
    telex_release = models.CharField(max_length=200, blank=True, null=True)
    # free_time_at_destination = models.CharField(max_length=200, blank=True, null=True)
    # vessels = models.CharField(max_length=200, blank=True, null=True)
    payment_credit = models.CharField(max_length=200, blank=True, null=True)
    # official_receipts = models.CharField(max_length=200, blank=True, null=True)
    other_notes = models.CharField(max_length=200, blank=True, null=True)
    # offer_validity = models.CharField(max_length=200, blank=True, null=True)

class FCLSeaQuotation(models.Model):
    """docstring for """

    ocean_freight = models.CharField(max_length=200, blank=True, null=True)
    pre_carriage = models.CharField(max_length=200, blank=True, null=True)
    thc_origin = models.CharField(max_length=200, blank=True, null=True)
    custom_clearance_origin = models.CharField(max_length=200, blank=True, null=True)
    documentation_origin = models.CharField(max_length=200, blank=True, null=True)
    xray = models.CharField(max_length=200, blank=True, null=True)
    baf = models.CharField(max_length=200, blank=True, null=True)
    caf = models.CharField(max_length=200, blank=True, null=True)
    others_origin = models.CharField(max_length=200, blank=True, null=True)
    documentation_destination = models.CharField(max_length=200, blank=True, null=True)
    thc_destination = models.CharField(max_length=200, blank=True, null=True)
    storage = models.CharField(max_length=200, blank=True, null=True)
    demurrage = models.CharField(max_length=200, blank=True, null=True)
    custom_clearance_destination = models.CharField(max_length=200, blank=True, null=True)
    road_cartage = models.CharField(max_length=200, blank=True, null=True)
    on_carriage = models.CharField(max_length=200, blank=True, null=True)
    others_destination = models.CharField(max_length=200, blank=True, null=True)
    container_fees = models.CharField(max_length=200, blank=True, null=True)
    delay = models.CharField(max_length=200, blank=True, null=True)
    official_receipts_selling = models.CharField(max_length=200, blank=True, null=True)

class Offer(models.Model):
    TYPE_CHOICES = (
        ('A', 'AIR'),
        ('S', 'SEA')
    )
    STATUS_CHOICES = (
        ('S', 'Sent To Client'),
        ('A', 'Accepted'),
        ('D', 'Done'),
        ('R', 'Rejected')
    )
    quotation = models.ForeignKey('main.Quotation', related_name='offers', blank=False, null=False)
    reference = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    sales_person = models.ForeignKey('authentication.User', related_name='offers', blank=True, null=True)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    client = models.ForeignKey('main.Client', related_name='offers', blank=True, null=True)
    air_quotation = models.OneToOneField('main.AirQuotation', related_name='offer', blank=True, null=True)
    sea_quotation = models.OneToOneField('main.SeaQuotation', related_name='offer', blank=True, null=True)
    fcl_quotation = models.OneToOneField('main.FCLSeaQuotation', related_name='offer', blank=True, null=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='S', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    terms = models.TextField(blank=True, null=True)
    class Meta:
        verbose_name = 'Offer'
        verbose_name_plural = 'Offers'
    def __str__(self):
        return self.client.client_name
