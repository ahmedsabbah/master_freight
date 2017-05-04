from django.shortcuts import render, redirect
from models import *
from authentication.models import User
from django.core.mail import send_mail
from django.core import serializers
from django.http.response import HttpResponse ,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.http import JsonResponse

def main(request):
    if not request.user.is_authenticated():
        return redirect('/login/')
    # if request.user.role == 'SA':
    #     return redirect('/sales/')
    # elif request.user.role == 'OP':
    #     return redirect('/operations/')
    # elif request.user.role == 'AC':
    #     return redirect('/accounting/')
    # elif request.user.role == 'HR':
    #     return redirect('/hr/')
    else:
        print 'authentic'
        return redirect('/admin/')
    # else:
    #     return redirect('/404/')

def hr(request):
    if not request.user.is_authenticated():
        return redirect('/login/')
    if request.user.role != 'HR':
        return redirect('/')
    return render(request, 'home_hr.html')

######## ADMIN #########

def getAdminWorkspace(request):
    if not request.user.is_authenticated():
        return redirect('/login/')
    # if request.user.role != 'AD':
    #     return redirect('/')
    return render(request, 'admin_workspace.html')

def getAdminTasks(request):
    if not request.user.is_authenticated():
        return redirect('/login/')

    if request.user.role == 'AC':
        offers = Offer.objects.filter(status='A')
        quotations = []
        for offer in offers:
            quotations.append(offer.quotation)
        context = {'quotations': quotations, 'offers': offers}
    elif request.user.role == 'OP':
        rate_requests = RateRequest.objects.all().exclude(status='DO')
        quotations = Quotation.objects.all().filter(operations_person=request.user).exclude(status='DO')
        context = {'rate_requests' : rate_requests, 'quotations' : quotations}
    elif request.user.role == 'SA':
        rate_requests = RateRequest.objects.filter(sales_person=request.user).exclude(status='DO')
        quotations = Quotation.objects.filter(sales_person=request.user).exclude(status='DO')
        offers = Offer.objects.filter(sales_person=request.user).exclude(status='D')
        context = {'rate_requests': rate_requests,'quotations': quotations, 'offers': offers}
    else:
        rate_requests = RateRequest.objects.all().exclude(status='DO')
        quotations = Quotation.objects.all().exclude(status='DO')
        offers = Offer.objects.all().exclude(status='D')
        context = {'rate_requests': rate_requests,'quotations': quotations, 'offers': offers}
    return render(request, 'admin_tasks.html', context )

def getAdminEmployees(request):
    if not request.user.is_authenticated():
        return redirect('/login/')
    if request.user.role != 'AD':
        return redirect('/')
    if request.method == 'POST':
        email = request.POST.get('email', None)
        role = request.POST.get('role', None)
        first_name = request.POST.get('first_name', None)
        last_name = request.POST.get('last_name', None)
        password = request.POST.get('password', None)

        if email and role and first_name and last_name and role:
            user = User(email=email, role=role, first_name=first_name, last_name=last_name)
            user.set_password(password)
            user.save()
        # else:
        #     response = HttpResponse(content_type='application/json')
        #     response.status_code = 400
        #     return response
    users = User.objects.all().exclude(role='AD')
    return render(request, 'admin_employees.html', {'users': users})

def getAdminCharts(request):
    if not request.user.is_authenticated():
        return redirect('/login/')
    if request.user.role != 'AD':
        return redirect('/')
    aif_requests = []
    lcl_requests = []
    fcl_requests = []
    offers_acc = []
    offers_rej = []
    offers_done = []
    trucker_numbers = []
    trucker_names = []
    for month in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']:
        aif_requests.append(RateRequest.objects.filter(created_date__month=month, type="AIF").count())
        lcl_requests.append(RateRequest.objects.filter(created_date__month=month, type="LCL").count())
        fcl_requests.append(RateRequest.objects.filter(created_date__month=month, type="FCL").count())

        offers_acc.append(Offer.objects.filter(created_date__month=month, status="A").count())
        offers_rej.append(Offer.objects.filter(created_date__month=month, status="R").count())
        offers_done.append(Offer.objects.filter(created_date__month=month, status="D").count())
    for trucker in Trucker.objects.all():
        trucker_numbers.append(trucker.quotations.count())
        trucker_names.append(trucker.company_name)
    return render(request, 'admin_charts.html', {'aif_requests': aif_requests,
    'lcl_requests': lcl_requests, 'fcl_requests': fcl_requests, 'offers_acc': offers_acc,
    'offers_rej': offers_rej, 'offers_done': offers_done, 'trucker_numbers': trucker_numbers, 'trucker_names': trucker_names})

################################

######## SALES ###############

def getSalesWorkspace(request):
    if not request.user.is_authenticated():
        return redirect('/login/')
    if request.user.role != 'SA':
        return redirect('/')
    return render(request, 'sales_workspace.html')

def getSalesTasks(request):
    if not request.user.is_authenticated():
        return redirect('/login/')
    if request.user.role != 'SA':
        return redirect('/')
    rate_requests = RateRequest.objects.filter(sales_person=request.user).exclude(status='DO')
    quotations = Quotation.objects.filter(sales_person=request.user).exclude(status='DO')
    offers = Offer.objects.filter(sales_person=request.user).exclude(status='DO')
    return render(request, 'sales_tasks.html', {'rate_requests': rate_requests.all(), 'quotations': quotations.all(), 'offers': offers.all()})

##############################

######## OPERATION #########

def getOperationsWorkspace(request):
    if not request.user.is_authenticated():
        return redirect('/login/')
    if request.user.role != 'OP':
        return redirect('/')
    return render(request, 'operations_workspace.html')

def getOperationsTasks(request):
    if not request.user.is_authenticated():
        return redirect('/login/')
    if request.user.role != 'OP':
        return redirect('/')
    rate_requests = RateRequest.objects.all().exclude(status='DO')
    quotations = Quotation.objects.all().exclude(status='DO')
    return render(request, 'operations_tasks.html', {'rate_requests': rate_requests, 'quotations': quotations})

############################
######### clients #########

def createClient(request):
    if not request.user.is_authenticated():
        return redirect('/login/')
    if request.user.role == 'AD' or request.user.role == 'SA':
        if request.method == 'POST':
            client_name = request.POST.get('client_name', None)
            client_type = request.POST.get('client_type', None)
            client_address = request.POST.get('client_address', None)
            commodity = request.POST.get('commodity', None)
            business_phone = request.POST.get('business_phone', None)
            alt_phone = request.POST.get('alt_phone', None)
            fax = request.POST.get('fax', None)
            email = request.POST.get('email', None)
            op_contact = request.POST.get('op_contact', None)
            op_job_title = request.POST.get('op_job_title', None)
            op_business_phone = request.POST.get('op_business_phone', None)
            op_email = request.POST.get('op_email', None)
            op_phone = request.POST.get('op_phone', None)
            finance_contact = request.POST.get('finance_contact', None)
            finance_job_title = request.POST.get('finance_job_title', None)
            finance_business_phone = request.POST.get('finance_business_phone', None)
            finance_email = request.POST.get('finance_email', None)
            finance_phone = request.POST.get('finance_phone', None)
            client_id_number = request.POST.get('client_id_number', None)
            credit_period = request.POST.get('credit_period', None)
            credit_limit = request.POST.get('credit_limit', None)
            reference_name = request.POST.get('reference_name', None)
            reference_phone = request.POST.get('reference_phone', None)
            notes = request.POST.get('notes', None)
            issued_by = request.POST.get('issued_by', None)
            authorized_by = request.POST.get('authorized_by', None)
            client = Client(client_name=client_name, client_type=client_type,
                client_address=client_address, commodity=commodity,
                business_phone=business_phone, alt_phone=alt_phone, fax=fax,
                email=email, op_contact=op_contact, op_job_title= op_job_title,
                op_business_phone=op_business_phone, op_email=op_email, op_phone=op_phone,
                finance_contact=finance_contact, finance_job_title=finance_job_title,
                finance_business_phone=finance_business_phone, finance_email=finance_email,
                finance_phone=finance_phone, client_id_number=client_id_number,
                credit_period=credit_period, credit_limit=credit_limit,
                reference_name=reference_name, reference_phone= reference_phone,
                notes=notes, issued_by=issued_by, authorized_by=authorized_by)
            client.save()
        return render(request, 'client_account.html')
    else:
        return redirect('/')

def listClient(request):
    if not request.user.is_authenticated():
        return redirect('/login/')

    clients = Client.objects.all()
    return render(request, 'client_view.html', {'clients': clients})


def getClient(request, pk):
    if not request.user.is_authenticated():
        return redirect('/login/')
    client = Client.objects.get(pk=pk)
    offers = Offer.objects.filter(client=client,status='D')
    return render(request, 'client_account_view.html', {'client': client, 'offers': offers})

def clientSelectHandler(request):
   client_id = request.GET["id"]
   client = Client.objects.get(pk=client_id)
   print client
   return JsonResponse({'company_name':client.client_name,
   'contact': client.op_contact, 'phone': client.op_phone, 'email': client.op_email,
   'extra_info': client.notes})

####### TRUCKER ########
def createTrucker(request):
    if not request.user.is_authenticated():
        return redirect('/login/')
    if request.user.role == 'AD' or request.user.role == 'SA':
        if request.method == 'POST':
            company_name = request.POST.get('company_name', None)
            address = request.POST.get('address', None)
            op_name = request.POST.get('op_name', None)
            op_phone = request.POST.get('op_phone', None)
            op_email = request.POST.get('op_email', None)
            acc_name = request.POST.get('acc_name', None)
            acc_phone = request.POST.get('acc_phone', None)
            acc_email = request.POST.get('acc_email', None)
            payment_terms = request.POST.get('payment_terms', None)
            special_requirements = request.POST.get('special_requirements', None)
            other_notes = request.POST.get('other_notes', None)

            trucker = Trucker(company_name=company_name, address=address,
                op_name=op_name, op_phone=op_phone,
                op_email=op_email, acc_name=acc_name, acc_phone=acc_phone,
                acc_email=acc_email, payment_terms=payment_terms,
                special_requirements= special_requirements, other_notes=other_notes)
            trucker.save()
        return render(request, 'trucker_add.html')
    else:
        return redirect('/')

def listTrucker(request):
    if not request.user.is_authenticated():
        return redirect('/login/')

    truckers = Trucker.objects.all()
    return render(request, 'trucker_list.html', {'truckers': truckers})


def getTrucker(request, pk):
    if not request.user.is_authenticated():
        return redirect('/login/')
    trucker = Trucker.objects.get(pk=pk)
    return render(request, 'trucker_detail.html', {'trucker': trucker})

####### ShippingLine ########

def createShippingLine(request):
    if not request.user.is_authenticated():
        return redirect('/login/')
    if request.user.role == 'AD':
        if request.method == 'POST':
            name = request.POST.get('name', None)

            shipping_line = ShippingLine(name=name)
            shipping_line.save()

        return render(request, 'shipping_line_add.html')
    else:
        return redirect('/')

def listShippingLine(request):
    if not request.user.is_authenticated():
        return redirect('/login/')

    shipping_lines = ShippingLine.objects.all()
    return render(request, 'shipping_line_list.html', {'shipping_lines': shipping_lines})

####### Shipment Term ########

def createShipmentTerm(request):
    if not request.user.is_authenticated():
        return redirect('/login/')
    if request.method == 'POST':
        title = request.POST.get('title', None)
        ex_work = request.POST.get('ex_work', None)
        fas = request.POST.get('fas', None)
        fob = request.POST.get('fob', None)
        cf = request.POST.get('cnf', None)
        cif = request.POST.get('cif', None)
        others = request.POST.get('others', None)
        shipment_term = ShipmentTerm(title=title,ex_work=ex_work, fas=fas, fob=fob, cf=cf, cif=cif, others=others)
        shipment_term.save()

    return render(request, 'shipment_term_add.html')

def listShipmentTerm(request):
    if not request.user.is_authenticated():
        return redirect('/login/')

    shipment_terms = ShipmentTerm.objects.all()
    return render(request, 'shipment_term_list.html', {'shipment_terms': shipment_terms})


def getShipmentTerm(request, pk):
    if not request.user.is_authenticated():
        return redirect('/login/')
    shipment_term = ShipmentTerm.objects.get(pk=pk)
    return render(request, 'shipment_term_detail.html', {'shipment_term': shipment_term})

####### Rate Request #########

def getAIFRateRequest(request):
    if not request.user.is_authenticated():
        return redirect('/login/')
    # if request.user.role == 'SA':
    #     return render(request, 'sales_rate_request_aif.html')
    if request.user.role == 'AD' or request.user.role == 'SA':
        clients = Client.objects.all()
        shipment_terms = ShipmentTerm.objects.all()
        shipping_lines = ShippingLine.objects.all()
        return render(request, 'admin_rate_request_aif.html', {'clients': clients,
        'shipment_terms': shipment_terms, 'shipping_lines': shipping_lines})
    else:
        return redirect('/')

def getFCLRateRequest(request):
    if not request.user.is_authenticated():
        return redirect('/login/')
    # if request.user.role == 'SA':
    #     return render(request, 'sales_rate_request_fcl.html')
    if request.user.role == 'AD' or request.user.role == 'SA':
        clients = Client.objects.all()
        shipment_terms = ShipmentTerm.objects.all()
        shipping_lines = ShippingLine.objects.all()
        return render(request, 'admin_rate_request_fcl.html',{'clients': clients,
         'shipment_terms': shipment_terms, 'shipping_lines': shipping_lines})
    else:
        return redirect('/')

def getLCLRateRequest(request):
    if not request.user.is_authenticated():
        return redirect('/login/')
    # if request.user.role == 'SA':
    #     return render(request, 'sales_rate_request_lcl.html')
    if request.user.role == 'AD' or request.user.role == 'SA':
        clients = Client.objects.all()
        shipment_terms = ShipmentTerm.objects.all()
        return render(request, 'admin_rate_request_lcl.html',{'clients': clients, 'shipment_terms': shipment_terms})
    else:
        return redirect('/')

def postRateRequest(request):
    if not request.user.is_authenticated():
        return redirect('/login/')
    if request.user.role != 'SA' and request.user.role != 'AD':
        return redirect('/')
    if request.method != 'POST':
        return redirect('/404/')

    sales_person = request.user
    type = request.POST.get('type', None)
    client = Client.objects.get(pk=request.POST.get('client', None))
    shipment_term = ShipmentTerm.objects.get(pk=request.POST.get('shipment_term', None))
    # name = request.POST.get('client_name', None)
    # company_name = request.POST.get('company_name', None)
    # contact = request.POST.get('contact', None)
    # phone = request.POST.get('phone', None)
    # email = request.POST.get('email', None)
    # extra_information = request.POST.get('extra_info', None)
    # client = Client(name=name, company_name=company_name, contact=contact, phone=phone, email=email, extra_information=extra_information)
    # client.save()

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

        preferred_shipping_line = ShippingLine.objects.get(pk=request.POST.get('preferred_shipping_line', None))
        other_shipping_line = ShippingLine.objects.get(pk=request.POST.get('other_shipping_line', None))

        rate_request = RateRequest(sales_person=sales_person, type=type,
        client=client, destination=destination, final_delivery_destination=final_delivery_destination,
        required_delivery_time_within=required_delivery_time_within,
        imo_class=imo_class, shipment_term=shipment_term, preferred_shipping_line=preferred_shipping_line,
        other_shipping_line=other_shipping_line, aif_cargo_details=aif_cargo_details,
        payment_term=payment_term, special_instructions=special_instructions)
        rate_request.save()

    elif type == 'FCL':
        container_type = request.POST.get('container_type', None)
        quantity = request.POST.get('quantity', None)
        commodity = request.POST.get('commodity', None)
        gross_weight = request.POST.get('gross_weight', None)
        net_weight = request.POST.get('net_weight', None)
        fcl_cargo_details = FCLCargoSales(container_type=container_type, quantity=quantity, commodity=commodity, gross_weight=gross_weight, net_weight=net_weight)
        fcl_cargo_details.save()


        preferred_shipping_line = ShippingLine.objects.get(pk=request.POST.get('preferred_shipping_line', None))
        other_shipping_line = ShippingLine.objects.get(pk=request.POST.get('other_shipping_line', None))

        rate_request = RateRequest(sales_person=sales_person, type=type,
         client=client, destination=destination, final_delivery_destination=final_delivery_destination,
          required_delivery_time_within=required_delivery_time_within,
          imo_class=imo_class, shipment_term=shipment_term,
          fcl_cargo_details=fcl_cargo_details, preferred_shipping_line=preferred_shipping_line,
          other_shipping_line=other_shipping_line, payment_term=payment_term,
          special_instructions=special_instructions)
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

    if request.user.role == 'SA' or request.user.role == 'AD':
        return redirect('/admin/tasks/')
    else:
        return redirect('/')

def editRateRequest(request, pk):
    if not request.user.is_authenticated():
        return redirect('/login/')
    if request.method != 'POST':
        return redirect('/404/')
    try:
        rate_request = RateRequest.objects.get(pk=pk)
        if request.user.role == 'AD' or (request.user.role == 'SA' and rate_request.sales_person.id == request.user.id):
            rate_request.status = request.POST.get('status', rate_request.status)
            rate_request.sales_person = request.POST.get('sales_person', rate_request.sales_person)
            rate_request.save()
            return HttpResponse(content_type='application/json')
        else:
            response = HttpResponse(content_type='application/json')
            response.status_code = 401
            return response
    except RateRequest.DoesNotExist:
        response = HttpResponse(content_type='application/json')
        response.status_code = 404
        return response

def viewRateRequest(request, pk):
    if not request.user.is_authenticated():
        return redirect('/login/')
    try:
        rate_request = RateRequest.objects.get(pk=pk)
        if request.user.role == 'AD' or request.user.role == 'SA' or request.user.role =='OP':
            if rate_request.type == 'AIF':
                return render(request, 'admin_rate_request_aif_view.html', { 'rate_request': rate_request })
            elif rate_request.type == 'FCL':
                return render(request, 'admin_rate_request_fcl_view.html', { 'rate_request': rate_request })
            elif rate_request.type == 'LCL':
                return render(request, 'admin_rate_request_lcl_view.html', { 'rate_request': rate_request })
        return redirect('/')
    except RateRequest.DoesNotExist:
        return redirect('/404/')

def deleteRateRequest(request, pk):
    if not request.user.is_authenticated():
        return redirect('/login/')
    try:
        if request.user.role == 'AD' or (request.user.role == 'SA' and rate_request.sales_person.id == request.user.id):
            rate_request = RateRequest.objects.get(pk=pk)
            rate_request.delete()
            if request.user.role == 'AD':
                return HttpResponseRedirect('/admin/tasks')
            else:
                return HttpResponseRedirect('/sales/tasks')
        else:
            response = HttpResponse(content_type='application/json')
            response.status_code = 401
            return response
    except RateRequest.DoesNotExist:
        response = HttpResponse(content_type='application/json')
        response.status_code = 404
        return response

############################


######## OFFER #############

def getAirOffer(request, pk):
    if not request.user.is_authenticated():
        return redirect('/login/')
    try:
        quotation = Quotation.objects.get(pk=pk)
        if request.user.role == 'AD' or 'SA':
            truckers = Trucker.objects.all()
            return render(request, 'admin_offer_air.html', { 'quotation': quotation, 'truckers': truckers })
        else:
            return redirect('/')
    except Quotation.DoesNotExist:
        return redirect('/404/')

def getSeaOffer(request, pk):
    if not request.user.is_authenticated():
        return redirect('/login/')
    try:
        quotation = Quotation.objects.get(pk=pk)
        if request.user.role == 'AD' or 'SA':
            shipping_lines = ShippingLine.objects.all()
            return render(request, 'admin_offer_sea.html', { 'quotation': quotation , 'shipping_lines': shipping_lines})
        else:
            return redirect('/')
    except RateRequest.DoesNotExist:
        return redirect('/404/')


def postOffer(request):
    if not request.user.is_authenticated():
        return redirect('/login/')
    if request.user.role != 'SA' and request.user.role != 'AD':
        return redirect('/')
    if request.method != 'POST':
        return redirect('/404/')

    type = request.POST.get('type', None)
    sales_person = request.user

    quotation_id = request.POST.get('quotation', None)
    if quotation_id == None:
        return redirect('/400/')
    try:
        quotation = Quotation.objects.get(pk=quotation_id)
    except Quotation.DoesNotExist:
        return redirect('/404/')

    client = quotation.client

    admins = User.objects.filter(role='AD')
    email_list = [];
    for admin in admins:
        email_list.append(admin.email)
    email_list.append(sales_person.email)
    print email_list
    if type == 'A':
        air_freight_kg = request.POST.get('air_freight_kg', None)
        fuel_sur_charge_kg = request.POST.get('fuel_sur_charge_kg', None)
        security_fees_kg = request.POST.get('security_fees_kg', None)
        exw_charges = request.POST.get('exw_charges', None)
        screening_fees = request.POST.get('screening_fees', None)
        storage = request.POST.get('storage', None)
        inland = Trucker.objects.get(pk=request.POST.get('inland', None))
        packing = request.POST.get('packing', None)
        taxes_duties = request.POST.get('taxes_duties', None)
        handling_fees = request.POST.get('handling_fees', None)
        official_receipts = request.POST.get('official_receipts', None)
        p_share = request.POST.get('p_share', None)
        other_notes = request.POST.get('other_notes', None)
        offer_validity = request.POST.get('offer_validity', None)
        air_quotation = AirQuotation(air_freight_kg=air_freight_kg, fuel_sur_charge_kg=fuel_sur_charge_kg, security_fees_kg=security_fees_kg, exw_charges=exw_charges, screening_fees=screening_fees, storage=storage, inland=inland, packing=packing, taxes_duties=taxes_duties, handling_fees=handling_fees, official_receipts=official_receipts, p_share=p_share, other_notes=other_notes, offer_validity=offer_validity)
        air_quotation.save()

        offer = Offer(quotation=quotation, type=type, sales_person=sales_person, client=client, air_quotation=air_quotation)
        offer.save()

        # quotation.sales_person = sales_person
        # quotation.save()
        msg_plain = render_to_string('./offerEmail.txt', {'offer': offer})
        msg_html = render_to_string('./offerEmail.html', {'offer': offer})
        send_mail(
            "Master Freight Offer",
            msg_plain,
            request.user.email,
            email_list,
            html_message=msg_html,
            fail_silently=False,
        )

    else:
        shipping_line = ShippingLine.objects.get(pk=request.POST.get('shipping_line', None))
        ocean_freight = request.POST.get('ocean_freight', None)
        thc = request.POST.get('thc', None)
        transporation = request.POST.get('transporation', None)
        transfer = request.POST.get('transfer', None)
        clearance = request.POST.get('clearance', None)
        bl_fees = request.POST.get('bl_fees', None)
        telex_release = request.POST.get('telex_release', None)
        free_time_at_destination = request.POST.get('free_time_at_destination', None)
        vessels = request.POST.get('vessels', None)
        payment_credit = request.POST.get('payment_credit', None)
        official_receipts = request.POST.get('official_receipts', None)
        other_notes = request.POST.get('other_notes', None)
        offer_validity = request.POST.get('offer_validity', None)
        sea_quotation = SeaQuotation(shipping_line=shipping_line, ocean_freight=ocean_freight, thc=thc, transporation=transporation, transfer=transfer, clearance=clearance, bl_fees=bl_fees, telex_release=telex_release, free_time_at_destination=free_time_at_destination, vessels=vessels, payment_credit=payment_credit, official_receipts=official_receipts, other_notes=other_notes, offer_validity=offer_validity)
        sea_quotation.save()

        offer = Offer(quotation=quotation, type=type, sales_person=sales_person, client=client, sea_quotation=sea_quotation)
        offer.save()

        quotation.sales_person = sales_person
        quotation.save()

        msg_plain = render_to_string('./offerSeaEmail.txt', {'offer': offer})
        msg_html = render_to_string('./offerSeaEmail.html', {'offer': offer})
        send_mail(
            "Master Freight Offer",
            msg_plain,
            request.user.email,
            email_list,
            html_message=msg_html,
            fail_silently=False,
        )

    if request.user.role == 'AD' or request.user.role == 'SA':
        return redirect('/admin/tasks/')
    else:
        return redirect('/')

def editOffer(request, pk):
    if not request.user.is_authenticated():
        return redirect('/login/')
    if request.method != 'POST':
        return redirect('/404/')
    try:
        offer = Offer.objects.get(pk=pk)
        if request.user.role == 'AD' or (request.user.role == 'SA' and offer.sales_person.id == request.user.id):

            offer.status = request.POST.get('status', offer.status)
            # offer.sales_person = request.POST.get('sales_person', offer.sales_person)
            offer.save()
            return HttpResponseRedirect('/admin/tasks')
        else:
            response = HttpResponse(content_type='application/json')
            response.status_code = 401
            return response
    except Offer.DoesNotExist:
        response = HttpResponse(content_type='application/json')
        response.status_code = 404
        return response

def viewOffer(request, pk):
    if not request.user.is_authenticated():
        return redirect('/login/')
    try:
        offer = Offer.objects.get(pk=pk)
        print offer.reference
        if request.user.role == 'AD' or (request.user.role == 'SA' and offer.sales_person.id == request.user.id):
            eligible = True
            if offer.type == 'A':
                return render(request, 'admin_offer_air_view.html', { 'offer': offer,  'eligible': eligible })
            elif offer.type == 'S':
                return render(request, 'admin_offer_sea_view.html', { 'offer': offer , 'eligible': eligible})
        elif request.user.role == 'AC' and offer.status == 'A':
            eligible = False
            if offer.type == 'A':
                return render(request, 'admin_offer_air_view.html', { 'offer': offer,  'eligible': eligible })
            elif offer.type == 'S':
                return render(request, 'admin_offer_sea_view.html', { 'offer': offer , 'eligible': eligible})

        else:
            return redirect('/')
    except Offer.DoesNotExist:
        return redirect('/404/')

def deleteOffer(request, pk):
    if not request.user.is_authenticated():
        return redirect('/login/')
    try:
        offer = Offer.objects.get(pk=pk)
        if request.user.role == 'AD' or (request.user.role == 'SA' and offer.sales_person.id == request.user.id):
            offer = Offer.objects.get(pk=pk)
            offer.delete()
            if request.user.role == 'AD' or request.user.role == 'SA':
                return HttpResponseRedirect('/admin/tasks')
            else:
                return redirect('/')
        else:
            response = HttpResponse(content_type='application/json')
            response.status_code = 401
            return response
    except Offer.DoesNotExist:
        response = HttpResponse(content_type='application/json')
        response.status_code = 404
        return response

def trackOffer(request, pk):
    try:
        offer = Offer.objects.get(reference=pk)
        if offer.type == 'A':
            return render(request, 'track_offer_air_view.html', { 'offer': offer })
        elif offer.type == 'S':
            return render(request, 'track_offer_sea_view.html', { 'offer': offer })

        else:
            return redirect('/')
    except Offer.DoesNotExist:
        return redirect('/404/')
##################################

######### Quotation ##############

def getAIFQuotation(request, pk):
    if not request.user.is_authenticated():
        return redirect('/login/')
    try:
        rate_request = RateRequest.objects.get(pk=pk)
        if request.user.role == 'OP' or request.user.role == 'AD':
            return render(request, 'admin_quotations_aif.html', { 'rate_request': rate_request })
        else:
            return redirect('/')
    except RateRequest.DoesNotExist:
        return redirect('/404/')

def getFCLQuotation(request, pk):
    if not request.user.is_authenticated():
        return redirect('/login/')
    try:
        rate_request = RateRequest.objects.get(pk=pk)

        if request.user.role == 'AD' or request.user.role == 'OP':
            shipping_lines = ShippingLine.objects.all()
            return render(request, 'admin_quotations_fcl.html', { 'rate_request': rate_request,
             'shipping_lines': shipping_lines })
        else:
            return redirect('/')
    except RateRequest.DoesNotExist:
        return redirect('/404/')

def getLCLQuotation(request, pk):
    if not request.user.is_authenticated():
        return redirect('/login/')
    try:
        rate_request = RateRequest.objects.get(pk=pk)
        if request.user.role == 'AD' or request.user.role == 'OP':
            shipping_lines = ShippingLine.objects.all()
            return render(request, 'admin_quotations_lcl.html', { 'rate_request': rate_request,
            'shipping_lines': shipping_lines  })
        else:
            return redirect('/')
    except RateRequest.DoesNotExist:
        return redirect('/404/')

def postQuotation(request):
    if not request.user.is_authenticated():
        return redirect('/login/')
    if request.user.role != 'OP' and request.user.role != 'AD':
        return redirect('/')
    if request.method != 'POST':
        return redirect('/404/')

    operations_person = request.user
    type = request.POST.get('type', None)

    rate_request_id = request.POST.get('rate_request', None)
    if rate_request_id == None:
        return redirect('/400/')
    try:
        rate_request = RateRequest.objects.get(pk=rate_request_id)
    except RateRequest.DoesNotExist:
        return redirect('/404/')

    client = rate_request.client
    sales_person = rate_request.sales_person

    arrival_date = request.POST.get('arrival_date', None)
    departure_date = request.POST.get('departure_date', None)

    # port_of_loading = request.POST.get('port_of_loading', None)
    # loading_location_type = request.POST.get('location_type_loading', None)
    # port_of_discharge = request.POST.get('port_of_discharge', None)
    # discharge_location_type = request.POST.get('location_type_discharge', None)
    # destination = Destination(port_of_loading=port_of_loading, loading_location_type=loading_location_type, port_of_discharge=port_of_discharge, discharge_location_type=discharge_location_type)
    # destination.save()

    destination = rate_request.destination

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
        arrival_date = request.POST.get('arrival_date', None)
        mawb_number = request.POST.get('mawb', None)
        hawb_number = request.POST.get('hawb', None)

        aif_cargo_details = AIFCargoOperations(commodity=commodity,
        num_of_packages=num_of_packages, actual_weight=actual_weight,
        chargeable_weight=chargeable_weight, dimensions=dimensions, air_line=air_line,
        transit_time=transit_time, route=route,
        mawb_number=mawb_number, hawb_number=hawb_number)
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

        quotation = Quotation(arrival_date=arrival_date, departure_date=departure_date, rate_request=rate_request, sales_person=sales_person, operations_person=operations_person, type=type, client=client, destination=destination, aif_cargo_details=aif_cargo_details, aif_quotation=aif_quotation, special_instructions=special_instructions)
        quotation.save()

    elif type == 'FCL':
        agent_details = request.POST.get('agent_details', None)

        shipping_line = ShippingLine.objects.get(pk=request.POST.get('shipping_line', None))
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

        free_time_at_destination = request.POST.get('free_time_at_destination', None)
        vessels_available = request.POST.get('vessels_available', None)
        route = request.POST.get('route', None)
        transit_time = request.POST.get('transit_time', None)
        offer_validity = request.POST.get('offer_validity', None)
        extra_notes = ExtraNotes(free_time_at_destination=free_time_at_destination, vessels_available=vessels_available, route=route, transit_time=transit_time, offer_validity=offer_validity)
        extra_notes.save()

        quotation = Quotation(arrival_date=arrival_date, departure_date=departure_date, rate_request=rate_request, sales_person=sales_person, operations_person=operations_person, type=type, client=client, destination=destination, special_instructions=special_instructions, agent_details=agent_details, fcl_cargo_details=fcl_cargo_details, fcl_quotation=fcl_quotation, extra_notes=extra_notes)
        quotation.save()

    else:
        agent_details = request.POST.get('agent_details', None)
        co_loader = request.POST.get('co_loader', None)

        shipping_line = ShippingLine.objects.get(pk=request.POST.get('shipping_line', None))
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
        vessels_available = request.POST.get('vessels_available', None)
        route = request.POST.get('route', None)
        transit_time = request.POST.get('transit_time', None)
        offer_validity = request.POST.get('offer_validity', None)
        extra_notes = ExtraNotes(free_time_at_destination=free_time_at_destination, vessels_available=vessels_available, route=route, transit_time=transit_time, offer_validity=offer_validity)
        extra_notes.save()

        quotation = Quotation(arrival_date=arrival_date, departure_date=departure_date,rate_request=rate_request, sales_person=sales_person, operations_person=operations_person, type=type, client=client, destination=destination, special_instructions=special_instructions, agent_details=agent_details, co_loader=co_loader, lcl_cargo_details=lcl_cargo_details, lcl_quotation=lcl_quotation, extra_notes=extra_notes)
        quotation.save()
    if request.user.role == 'AD' or request.user.role == 'OP':
        return redirect('/admin/tasks/')
    else:
        return redirect('/')

def editQuotation(request, pk):
    if not request.user.is_authenticated():
        return redirect('/login/')
    if request.method != 'POST':
        return redirect('/404/')
    try:
        quotation = Quotation.objects.get(pk=pk)
        if request.user.role == 'AD' or (request.user.role == 'OP' and quotation.operations_person.id == request.user.id):
            quotation.current_location = request.POST.get('current_location', None)
            quotation.departure_date = request.POST.get('departure_date', None)
            quotation.arrival_date = request.POST.get('arrival_date', None)
            quotation.save()
            return HttpResponseRedirect('/admin/tasks')
        else:
            return HttpResponseRedirect('/admin/tasks')
    except Quotation.DoesNotExist:
        response = HttpResponse(content_type='application/json')
        response.status_code = 404
        return response

def viewQuotation(request, pk):
    if not request.user.is_authenticated():
        return redirect('/login/')
    try:
        quotation = Quotation.objects.get(pk=pk)
        if request.user.role == 'AD' or request.user.role == 'SA' or request.user.role == 'OP' or (request.user.role == 'AC' and quotation.offers.first().status == 'A'):
            if quotation.type == 'AIF':
                return render(request, 'admin_quotations_aif_view.html', { 'quotation': quotation })
            elif quotation.type == 'FCL':
                return render(request, 'admin_quotations_fcl_view.html', { 'quotation': quotation })
            elif quotation.type == 'LCL':
                return render(request, 'admin_quotations_lcl_view.html', { 'quotation': quotation })
        return redirect('/')
    except Quotation.DoesNotExist:
        return redirect('/404/')

def deleteQuotation(request, pk):
    if not request.user.is_authenticated():
        return redirect('/login/')
    try:
        quotation = Quotation.objects.get(pk=pk)
        if request.user.role == 'AD' or (request.user.role == 'OP' and quotation.operations_person.id == request.user.id):
            quotation = Quotation.objects.get(pk=pk)
            quotation.delete()
            if request.user.role == 'AD':
                return HttpResponseRedirect('/admin/tasks')
            else:
                return HttpResponseRedirect('/sales/tasks')
        else:
            response = HttpResponse(content_type='application/json')
            response.status_code = 401
            return response
    except Quotation.DoesNotExist:
        response = HttpResponse(content_type='application/json')
        response.status_code = 404
        return response

####################################

############ TOOLS #################

def contact(request):
    if not request.user.is_authenticated():
        return redirect('/login/')
    if request.method == 'POST':
        name = request.POST.get('name', None)
        title = request.POST.get('title', None)
        message = request.POST.get('message', None)
        if name and title and message:
            emails = []
            if request.user.role == 'AD':
                users = User.objects.all()
                for user in users:
                    emails.append(user.email)
            else:
                users = User.objects.filter(role="AD")
                for user in users:
                    emails.append(user.email)
            send_mail(
                title,
                message,
                request.user.email,
                emails,
                fail_silently=False,
            )
    return redirect('/')

def notFound(request):
    return render(request, '404.html')

def deleteTodo(request, pk):
    if not request.user.is_authenticated():
        response = HttpResponse(content_type='application/json')
        response.status_code = 401
        return response
    Todo.objects.filter(pk=pk).delete()
    todos = Todo.objects.filter(user=request.user)
    data = serializers.serialize("json", todos)
    return HttpResponse(data, content_type='application/json')

@csrf_exempt
def todos(request):
    if not request.user.is_authenticated():
        response = HttpResponse(content_type='application/json')
        response.status_code = 401
        return response
    if request.method == 'POST':
        text = request.POST.get('text', None)
        if text:
            todo = Todo(user=request.user, text=text)
            todo.save();
            # todos = Todo.objects.filter(user=request.user)
            data = serializers.serialize("json", [ todo, ])
            return HttpResponse(data, content_type='application/json')
        else:
            response = HttpResponse(content_type='application/json')
            response.status_code = 400
            return response
    elif request.method == 'GET':
        todos = Todo.objects.filter(user=request.user)
        data = serializers.serialize("json", todos)
        return HttpResponse(data, content_type='application/json')
    else:
        response = HttpResponse(content_type='application/json')
        response.status_code = 404
        return response

####################################
