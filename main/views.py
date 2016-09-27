from django.shortcuts import render, redirect
from models import Client, Destination, FinalDeliveryDestination, AIFCargoSales, FCLCargoSales, LCLCargoSales, ShippingLine, IMOClass, ShipmentTerm, RateRequest, AIFCargoOperations, FCLCargoOperations, LCLCargoOperations, AIFQuotation, FCLQuotation, LCLQuotation, ExtraNotes, Quotation
from authentication.views import User

def main(request):
    if not request.user.is_authenticated():
        return redirect('/login/')
    if request.user.role == 'SA':
        return redirect('/sales/')
    elif request.user.role == 'OP':
        return redirect('/operations/')
    elif request.user.role == 'AC':
        return redirect('/accounting/')
    elif request.user.role == 'HR':
        return redirect('/hr/')
    elif request.user.role == 'AD':
        return redirect('/admin/')
    else:
        return redirect('/404/')

def notFound(request):
    return render(request, '404.html')

def sales(request):
    if not request.user.is_authenticated():
        return redirect('/login/')
    if request.user.role != 'SA':
        return redirect('/')
    return render(request, 'home_sales.html')

def operations(request):
    if not request.user.is_authenticated():
        return redirect('/login/')
    if request.user.role != 'OP':
        return redirect('/')
    return render(request, 'home_operations.html')

def accounting(request):
    if not request.user.is_authenticated():
        return redirect('/login/')
    if request.user.role != 'AC':
        return redirect('/')
    return render(request, 'home_accounting.html')

def hr(request):
    if not request.user.is_authenticated():
        return redirect('/login/')
    if request.user.role != 'HR':
        return redirect('/')
    return render(request, 'home_hr.html')

def admin(request):
    if not request.user.is_authenticated():
        return redirect('/login/')
    if request.user.role != 'AD':
        return redirect('/')
    return render(request, 'home_admin.html')

def getAIFRateRequest(request):
    if not request.user.is_authenticated():
        return redirect('/login/')
    if request.user.role != 'SA':
        return redirect('/')
    return render(request, 'aif_rate_request.html')

def getFCLRateRequest(request):
    if not request.user.is_authenticated():
        return redirect('/login/')
    if request.user.role != 'SA':
        return redirect('/')
    return render(request, 'fcl_rate_request.html')

def getLCLRateRequest(request):
    if not request.user.is_authenticated():
        return redirect('/login/')
    if request.user.role != 'SA':
        return redirect('/')
    return render(request, 'lcl_rate_request.html')

def postRateRequest(request):
    if not request.user.is_authenticated():
        return redirect('/login/')
    if request.user.role != 'SA':
        return redirect('/')
    if request.method != 'POST':
        return redirect('/404/')

    sales_person = request.user
    type = request.POST.get('type', None)

    name = request.POST.get('client_name', None)
    company_name = request.POST.get('company_name', None)
    contact = request.POST.get('contact', None)
    phone = request.POST.get('phone', None)
    email = request.POST.get('email', None)
    extra_information = request.POST.get('extra_info', None)
    client = Client(name=name, company_name=company_name, contact=contact, phone=phone, email=email, extra_info=extra_info)
    client.save()

    port_of_loading = request.POST.get('port_of_loading', None)
    loading_location_type = request.POST.get('location_type_loading', None)
    port_of_discharge = request.POST.get('port_of_discharge', None)
    discharge_location_type = request.POST.get('location_type_discharge', None)
    destination = Destination(port_of_loading=port_of_loading, loading_location_type=loading_location_type, port_of_discharge=port_of_discharge, discharge_location_type=discharge_location_type)
    destination.save()

    address = request.POST.get('address', None)
    contact_person = request.POST.get('contact_person', None)
    contact_person_extra = request.POST.get('contact_person_extra', None)
    final_delivery_destination = FinalDeliveryDestination(address=address, contact_person=contact_person, contact_person_extra=contact_person_extra)
    final_delivery_destination.save()

    required_delivery_time_within = request.POST.get('delivery_time', None)

    hazardous = request.POST.get('hazardous', None)
    non_hazardous = request.POST.get('non_hazardous', None)
    imo_class = IMOClass(hazardous=hazardous, non_hazardous=non_hazardous)
    imo_class.save()

    ex_work = request.POST.get('ex_work', None)
    fas = request.POST.get('fas', None)
    fob = request.POST.get('fob', None)
    cf = request.POST.get('cnf', None)
    cif = request.POST.get('cif', None)
    others = request.POST.get('others', None)
    shipment_term = ShipmentTerm(ex_work=ex_work, fas=fas, fob=fob, cf=cf, cif=cif, others=others)
    shipment_term.save()

    payment_term = request.POST.get('payment_term', None)
    special_instructions = request.POST.get('special_instructions', None)

    if type == 'AIF':
        quantity = request.POST.get('quantity', None)
        commodity = request.POST.get('commodity', None)
        gross_weight = request.POST.get('gross_weight', None)
        net_weight = request.POST.get('net_weight', None)
        pieces = request.POST.get('pieces', None)
        packing = request.POST.get('packing', None)
        dimensions = request.POST.get('dimensions', None)
        aif_cargo_details = AIFCargoSales(quantity=quantity, commodity=commodity, gross_weight=gross_weight, net_weight=net_weight, pieces=pieces, packing=packing, dimensions=dimensions)
        aif_cargo_details.save()

        prefered = request.POST.get('prefered', None)
        any = request.POST.get('any', None)
        shipping_line = ShippingLine(prefered=prefered, any=any)
        shipping_line.save()

        rate_request = RateRequest(sales_person=sales_person, type=type, client=client, destination=destination, final_delivery_destination=final_delivery_destination, required_delivery_time_within=required_delivery_time_within, imo_class=imo_class, shipment_term=shipment_term, aif_cargo_details=aif_cargo_details, shipping_line=shipping_line, payment_term=payment_term, special_instructions=special_instructions)
        rate_request.save()

    elif type == 'FCL':
        container_type = request.POST.get('container_type', None)
        quantity = request.POST.get('quantity', None)
        commodity = request.POST.get('commodity', None)
        gross_weight = request.POST.get('gross_weight', None)
        net_weight = request.POST.get('net_weight', None)
        fcl_cargo_details = FCLCargoSales(container_type=container_type, quantity=quantity, commodity=commodity, gross_weight=gross_weight, net_weight=net_weight)
        fcl_cargo_details.save()

        prefered = request.POST.get('prefered', None)
        any = request.POST.get('any', None)
        shipping_line = ShippingLine(prefered=prefered, any=any)
        shipping_line.save()

        rate_request = RateRequest(sales_person=sales_person, type=type, client=client, destination=destination, final_delivery_destination=final_delivery_destination, required_delivery_time_within=required_delivery_time_within, imo_class=imo_class, shipment_term=shipment_term, fcl_cargo_details=fcl_cargo_details, shipping_line=shipping_line, payment_term=payment_term, special_instructions=special_instructions)
        rate_request.save()

    else:
        quantity = request.POST.get('quantity', None)
        commodity = request.POST.get('commodity', None)
        gross_weight = request.POST.get('gross_weight', None)
        net_weight = request.POST.get('net_weight', None)
        pieces = request.POST.get('pieces', None)
        packing = request.POST.get('packing', None)
        lcl_cargo_details = LCLCargoSales(quantity=quantity, commodity=commodity, gross_weight=gross_weight, net_weight=net_weight, pieces=pieces, packing=packing)
        lcl_cargo_details.save()

        rate_request = RateRequest(sales_person=sales_person, type=type, client=client, destination=destination, final_delivery_destination=final_delivery_destination, required_delivery_time_within=required_delivery_time_within, imo_class=imo_class, shipment_term=shipment_term, lcl_cargo_details=lcl_cargo_details, payment_term=payment_term, special_instructions=special_instructions)
        rate_request.save()

    return redirect('/')

def getAIFQuotation(request):
    if not request.user.is_authenticated():
        return redirect('/login/')
    if request.user.role != 'OP':
        return redirect('/')
    return render(request, 'quotations_aif.html')

def getFCLQuotation(request):
    if not request.user.is_authenticated():
        return redirect('/login/')
    if request.user.role != 'OP':
        return redirect('/')
    return render(request, 'quotations_fcl.html')

def getLCLQuotation(request):
    if not request.user.is_authenticated():
        return redirect('/login/')
    if request.user.role != 'OP':
        return redirect('/')
    return render(request, 'quotations_lcl.html')

def postQuotation(request):
    if not request.user.is_authenticated():
        return redirect('/login/')
    if request.user.role != 'OP':
        return redirect('/')
    if request.method != 'POST':
        return redirect('/404/')

    operations_person = request.user
    type = request.POST.get('type', None)

    name = request.POST.get('client_name', None)
    company_name = request.POST.get('company_name', None)
    contact = request.POST.get('contact', None)
    phone = request.POST.get('phone', None)
    email = request.POST.get('email', None)
    extra_information = request.POST.get('extra_info', None)
    client = Client(name=name, company_name=company_name, contact=contact, phone=phone, email=email, extra_info=extra_info)
    client.save()

    port_of_loading = request.POST.get('port_of_loading', None)
    loading_location_type = request.POST.get('location_type_loading', None)
    port_of_discharge = request.POST.get('port_of_discharge', None)
    discharge_location_type = request.POST.get('location_type_discharge', None)
    destination = Destination(port_of_loading=port_of_loading, loading_location_type=loading_location_type, port_of_discharge=port_of_discharge, discharge_location_type=discharge_location_type)
    destination.save()

    special_instructions = request.POST.get('special_instructions', None)

    if type == 'AIF':
        commodity = request.POST.get('commodity', None)
        num_of_packages = request.POST.get('no_of_packages', None)
        actual_weight = request.POST.get('actual_weight', None)
        chargeable_weight = request.POST.get('chargeable_weight', None)
        dimensions = request.POST.get('dimensions', None)
        air_line = request.POST.get('air_line', None)
        transit_time = request.POST.get('transit_date', None)
        route = request.POST.get('route', None)
        departure_date = request.POST.get('departure_date', None)
        arrival_date = request.POST.get('arrival_date', None)
        mawb_number = request.POST.get('mawb', None)
        hawb_number = request.POST.get('hawb', None)

        aif_cargo_details = AIFCargoOperations(commodity=commodity, num_of_packages=num_of_packages, actual_weight=actual_weight, chargeable_weight=chargeable_weight, dimensions=dimensions, air_line=air_line, transit_time=transit_time, route=route, departure_date=departure_date, arrival_date=arrival_date, mawb_number=mawb_number, hawb_number=hawb_number)
        aif_cargo_details.save()

        air_freight_kg_net = request.POST.get('airfreight_net', None)
        air_freight_kg_selling = request.POST.get('airfreight_selling', None)
        fuel_sur_charge_kg_net = request.POST.get('fuel_surcharge_net', None)
        fuel_sur_charge_kg_selling = request.POST.get('fuel_surcharge_selling', None)
        security_fees_kg_net = request.POST.get('security_fees_net', None)
        security_fees_kg_selling = request.POST.get('security_fees_selling', None)
        exw_charges_net = request.POST.get('exw_charges_net', None)
        exw_charges_selling = request.POST.get('exw_charges_selling', None)
        screening_fees_net = request.POST.get('screening_fees_net', None)
        screening_fees_selling = request.POST.get('screening_fees_selling', None)
        storage_net = request.POST.get('storage_net', None)
        storage_selling = request.POST.get('storage_selling', None)
        inland_net = request.POST.get('inland_net', None)
        inland_selling = request.POST.get('inland_selling', None)
        packing_net = request.POST.get('packing_net', None)
        packing_selling = request.POST.get('packing_selling', None)
        taxes_duties_net = request.POST.get('taxes_n_duties_net', None)
        taxes_duties_selling = request.POST.get('taxes_n_duties_selling', None)
        handling_fees_net = request.POST.get('handling_fees_net', None)
        handling_fees_selling = request.POST.get('handling_fees_selling', None)
        p_share_net = request.POST.get('p_share_net', None)
        p_share_selling = request.POST.get('p_share_selling', None)

        aif_quotation = AIFQuotation(air_freight_kg_net=air_freight_kg_net, air_freight_kg_selling=air_freight_kg_selling, fuel_sur_charge_kg_net=fuel_sur_charge_kg_net, fuel_sur_charge_kg_selling=fuel_sur_charge_kg_selling, security_fees_kg_net=security_fees_kg_net, security_fees_kg_selling=security_fees_kg_selling, exw_charges_net=exw_charges_net, exw_charges_selling=exw_charges_selling, screening_fees_net=screening_fees_net, screening_fees_selling=screening_fees_selling, storage_net=storage_net, storage_selling=storage_selling, inland_net=inland_net, inland_selling=inland_selling, packing_net=packing_net, packing_selling=packing_selling, taxes_duties_net=taxes_duties_net, taxes_duties_selling=taxes_duties_selling, handling_fees_net=handling_fees_net, handling_fees_selling=handling_fees_selling, p_share_net=p_share_net, p_share_selling=p_share_selling)
        aif_quotation.save()

        quotation = Quotation(operations_person=operations_person, type=type, client=client, destination=destination, aif_cargo_details=aif_cargo_details, aif_quotation=aif_quotation, special_instructions=special_instructions)
        quotation.save()

    elif type == 'FCL':
        agent_details = request.POST.get('agent_details', None)

        shipping_line = request.POST.get('shipping_line', None)
        container_type = request.POST.get('container_type', None)
        quantity = request.POST.get('quantity', None)
        commodity = request.POST.get('commodity', None)
        gross_weight = request.POST.get('gross_weight', None)
        net_weight = request.POST.get('net_weight', None)
        fcl_cargo_details = FCLCargoOperations(shipping_line=shipping_line, container_type=container_type, quantity=quantity, commodity=commodity, gross_weight=gross_weight, net_weight=net_weight)
        fcl_cargo_details.save()

        ocean_freight_net = request.POST.get('ocean_freight_net', None)
        ocean_freight_selling = request.POST.get('ocean_freight_selling', None)
        thc_net = request.POST.get('thc_net', None)
        thc_selling = request.POST.get('thc_selling', None)
        transporation_net = request.POST.get('transportation_net', None)
        transporation_selling = request.POST.get('transportation_selling', None)
        transfer_net = request.POST.get('transfer_net', None)
        transfer_selling = request.POST.get('transfer_selling', None)
        clearance_pol_net = request.POST.get('clearance_pol_net', None)
        clearance_pol_selling = request.POST.get('clearance_pol_selling', None)
        clearance_pod_net = request.POST.get('clearance_pod_net', None)
        clearance_pod_selling = request.POST.get('clearance_pod_selling', None)
        bl_fees_net = request.POST.get('bl_fees_net', None)
        bl_fees_selling = request.POST.get('bl_fees_selling', None)
        telex_release_net = request.POST.get('telex_release_net', None)
        telex_release_selling = request.POST.get('telex_release_selling', None)
        ex_work_net = request.POST.get('ex_work_net', None)
        ex_work_selling = request.POST.get('ex_work_selling', None)
        official_receipts_net = request.POST.get('official_receipts_net', None)
        official_receipts_selling = request.POST.get('official_receipts_selling', None)
        fcl_quotation = FCLQuotation(ocean_freight_net=ocean_freight_net, ocean_freight_selling=ocean_freight_selling, thc_net=thc_net, thc_selling=thc_selling, transporation_net=transporation_net, transporation_selling=transporation_selling, transfer_net=transfer_net, transfer_selling=transfer_selling, clearance_pol_net=clearance_pol_net, clearance_pol_selling=clearance_pol_selling, clearance_pod_net=clearance_pod_net, clearance_pod_selling=clearance_pod_selling, bl_fees_net=bl_fees_net, bl_fees_selling=bl_fees_selling, telex_release_net=telex_release_net, telex_release_selling=telex_release_selling, ex_work_net=ex_work_net, ex_work_selling=ex_work_selling, official_receipts_net=official_receipts_net, official_receipts_selling=official_receipts_selling)
        fcl_quotation.save()

        free_time_at_destination = request.POST.get('free_time_destination', None)
        vessel_available = request.POST.get('vessels_available', None)
        route = request.POST.get('route', None)
        transit_time = request.POST.get('transit_time', None)
        offer_validity = request.POST.get('offer_validity', None)
        extra_notes = ExtraNotes(free_time_at_destination=free_time_at_destination, vessel_available=vessel_available, route=route, transit_time=transit_time, offer_validity=offer_validity)
        extra_notes.save()

        quotation = Quotation(operations_person=operations_person, type=type, client=client, destination=destination, special_instructions=special_instructions, agent_details=agent_details, fcl_cargo_details=fcl_cargo_details, fcl_quotation=fcl_quotation, extra_notes=extra_notes)
        quotation.save()

    else:
        agent_details = request.POST.get('agent_details', None)
        co_loader = request.POST.get('co_loader', None)

        shipping_line = request.POST.get('shipping_line', None)
        container_type = request.POST.get('container_type', None)
        num_of_packages = request.POST.get('number_of_packages', None)
        commodity = request.POST.get('commodity', None)
        gross_weight = request.POST.get('gross_weight', None)
        net_weight = request.POST.get('net_weight', None)
        dimensions_cbm = request.POST.get('dimensions_cbm', None)
        lcl_cargo_details = LCLCargoOperations(shipping_line=shipping_line, container_type=container_type, num_of_packages=num_of_packages, commodity=commodity, gross_weight=gross_weight, net_weight=net_weight, dimensions_cbm=dimensions_cbm)
        lcl_cargo_details.save()

        ocean_freight_net = request.POST.get('ocean_freight_net', None)
        ocean_freight_selling = request.POST.get('ocean_freight_selling', None)
        thc_net = request.POST.get('thc_net', None)
        thc_selling = request.POST.get('thc_selling', None)
        transporation_net = request.POST.get('transportation_net', None)
        transporation_selling = request.POST.get('transportation_selling', None)
        transfer_net = request.POST.get('transfer_net', None)
        transfer_selling = request.POST.get('transfer_selling', None)
        clearance_pol_net = request.POST.get('clearance_pol_net', None)
        clearance_pol_selling = request.POST.get('clearance_pol_selling', None)
        clearance_pod_net = request.POST.get('clearance_pod_net', None)
        clearance_pod_selling = request.POST.get('clearance_pod_selling', None)
        bl_fees_net = request.POST.get('bl_fees_net', None)
        bl_fees_selling = request.POST.get('bl_fees_selling', None)
        telex_release_net = request.POST.get('telex_release_net', None)
        telex_release_selling = request.POST.get('telex_release_selling', None)
        ex_work_net = request.POST.get('ex_work_net', None)
        ex_work_selling = request.POST.get('ex_work_selling', None)
        official_receipts_net = request.POST.get('official_receipts_net', None)
        official_receipts_selling = request.POST.get('official_receipts_selling', None)
        lcl_quotation = LCLQuotation(ocean_freight_net=ocean_freight_net, ocean_freight_selling=ocean_freight_selling, thc_net=thc_net, thc_selling=thc_selling, transporation_net=transporation_net, transporation_selling=transporation_selling, transfer_net=transfer_net, transfer_selling=transfer_selling, clearance_pol_net=clearance_pol_net, clearance_pol_selling=clearance_pol_selling, clearance_pod_net=clearance_pod_net, clearance_pod_selling=clearance_pod_selling, bl_fees_net=bl_fees_net, bl_fees_selling=bl_fees_selling, telex_release_net=telex_release_net, telex_release_selling=telex_release_selling, ex_work_net=ex_work_net, ex_work_selling=ex_work_selling, official_receipts_net=official_receipts_net, official_receipts_selling=official_receipts_selling)
        lcl_quotation.save()

        free_time_at_destination = request.POST.get('free_time_destination', None)
        vessel_available = request.POST.get('vessels_available', None)
        route = request.POST.get('route', None)
        transit_time = request.POST.get('transit_time', None)
        offer_validity = request.POST.get('offer_validity', None)
        extra_notes = ExtraNotes(free_time_at_destination=free_time_at_destination, vessel_available=vessel_available, route=route, transit_time=transit_time, offer_validity=offer_validity)
        extra_notes.save()

        quotation = Quotation(operations_person=operations_person, type=type, client=client, destination=destination, special_instructions=special_instructions, agent_details=agent_details, co_loader=co_loader, lcl_cargo_details=lcl_cargo_details, lcl_quotation=lcl_quotation, extra_notes=extra_notes)
        quotation.save()

    return redirect('/')
