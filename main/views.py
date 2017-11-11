from django.shortcuts import render, redirect
from models import *
from authentication.models import User
from django.core.mail import send_mail
from django.core import serializers
from django.http.response import HttpResponse ,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist


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
            print email
            print role
            user = User(email=email, role=role, first_name=first_name, last_name=last_name)
            print user
            user.set_password(password)
            user.save()
        # else:
        #     response = HttpResponse(content_type='application/json')
        #     response.status_code = 400
        #     return response

            # .exclude(role='AD')
    users = User.objects.all()
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
    shipping_line_numbers = []
    shipping_line_names = []
    total_offer_count = Offer.objects.count()
    if total_offer_count !=0:
        percentage_acc_count =round(Offer.objects.filter(status='A').count()/float(total_offer_count)*100)
        percentage_rej_count = round(Offer.objects.filter(status='R').count()/float(total_offer_count)*100)
        percentage_done_count = round(Offer.objects.filter(status='D').count()/float(total_offer_count)*100)
        percentage_pending_count = round(Offer.objects.filter(status='S').count()/float(total_offer_count)*100)
    else:
        percentage_acc_count = 0
        percentage_rej_count = 0
        percentage_done_count = 0
        percentage_pending_count = 0

    for month in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']:
        aif_requests.append(RateRequest.objects.filter(created_date__month=month, type="AIF").count())
        lcl_requests.append(RateRequest.objects.filter(created_date__month=month, type="LCL").count())
        fcl_requests.append(RateRequest.objects.filter(created_date__month=month, type="FCL").count())

        offers_acc.append(Offer.objects.filter(created_date__month=month, status="A").count())
        offers_rej.append(Offer.objects.filter(created_date__month=month, status="R").count())
        offers_done.append(Offer.objects.filter(created_date__month=month, status="D").count())

    for trucker in Trucker.objects.all():
        done_quotations = 0
        for trucker_offer in trucker.trucker_offers.all():
            for quotation in trucker_offer.aif_quotations.all():
                if quotation:
                    qots = Quotation.objects.filter(aif_quotation=quotation, status="DO").count()
                    done_quotations += qots
        trucker_numbers.append(done_quotations)
        trucker_names.append(trucker.company_name)


    for shipping_line in ShippingLine.objects.all():
        shipping_line_numbers.append(shipping_line.sea_rate_requests.count())
        shipping_line_names.append(shipping_line.name)
    return render(request, 'admin_charts.html', {'aif_requests': aif_requests,
    'lcl_requests': lcl_requests, 'fcl_requests': fcl_requests, 'offers_acc': offers_acc,
    'offers_rej': offers_rej, 'offers_done': offers_done, 'trucker_numbers': trucker_numbers, 'trucker_names': trucker_names,
    'shipping_line_numbers': shipping_line_numbers, 'shipping_line_names': shipping_line_names, 'total_offer_count': total_offer_count,
    'percentage_acc_count': percentage_acc_count, 'percentage_rej_count': percentage_rej_count, 'percentage_done_count': percentage_done_count,
    'percentage_pending_count': percentage_pending_count})

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
            extra_information = request.POST.get('extra_information', None)
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
                notes=notes, issued_by=issued_by, authorized_by=authorized_by,
                extra_information=extra_information)
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
    offers = Offer.objects.filter(client=client)
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
            special_requirements = request.POST.get('special_requirements', None)
            other_notes = request.POST.get('other_notes', None)

            trucker = Trucker(company_name=company_name, address=address,
                op_name=op_name, op_phone=op_phone,
                op_email=op_email, acc_name=acc_name, acc_phone=acc_phone,
                acc_email=acc_email,
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
    offers=[]
    trucker = Trucker.objects.get(pk=pk)
    air_quotations = AirQuotation.objects.filter(inland=trucker)
    for quot in air_quotations:
        # print quot.offer
        try:
            offers.append(quot.offer)
        except ObjectDoesNotExist:
            pass

    # offers = Offer.objects.filter(air_quotation__inline=trucker)
    return render(request, 'trucker_detail.html', {'trucker': trucker, 'offers': offers})

def deleteTrucker(request, pk):
    if not request.user.is_authenticated():
        return redirect('/login/')
    try:
        if request.user.role == 'AD':
            trucker = Trucker.objects.get(pk=pk)
            trucker.delete()
            return HttpResponseRedirect('/admin/tasks')
        else:
            response = HttpResponse(content_type='application/json')
            response.status_code = 401
            return response
    except Trucker.DoesNotExist:
        response = HttpResponse(content_type='application/json')
        response.status_code = 404
        return response
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

def getShippingLine(request, pk):
    if not request.user.is_authenticated():
        return redirect('/login/')
    offers=[]
    shipping_line = ShippingLine.objects.get(pk=pk)
    sea_quotations = SeaQuotation.objects.filter(shipping_line=shipping_line)
    for quot in sea_quotations:
        try:
            offers.append(quot.offer)
        except ObjectDoesNotExist:
            pass

    # offers = Offer.objects.filter(air_quotation__inline=trucker)
    return render(request, 'shipping_line_detail.html', {'shipping_line': shipping_line, 'offers': offers})

def deleteShippingLine(request, pk):
    if not request.user.is_authenticated():
        return redirect('/login/')
    try:
        if request.user.role == 'AD':
            shipping_line = ShippingLine.objects.get(pk=pk)
            shipping_line.delete()
            return HttpResponseRedirect('/shipping_line/list/')
        else:
            response = HttpResponse(content_type='application/json')
            response.status_code = 401
            return response
    except ShippingLine.DoesNotExist:
        response = HttpResponse(content_type='application/json')
        response.status_code = 404
        return response

####### PORT ########
def createPort(request):
    if not request.user.is_authenticated():
        return redirect('/login/')
    if request.user.role == 'AD':
        if request.method == 'POST':
            name = request.POST.get('name', None)

            port = Port(name=name)
            port.save()

        return render(request, 'port_add.html')
    else:
        return redirect('/')

def listPort(request):
    if not request.user.is_authenticated():
        return redirect('/login/')

    ports = Port.objects.all()
    return render(request, 'port_list.html', {'ports': ports})

def getPort(request, pk):
    if not request.user.is_authenticated():
        return redirect('/login/')

    port = Port.objects.get(pk=pk)
    return render(request, 'port_detail.html', {'port': port})

def deletePort(request, pk):
    if not request.user.is_authenticated():
        return redirect('/login/')
    try:
        if request.user.role == 'AD':
            port = Port.objects.get(pk=pk)
            port.delete()
            return HttpResponseRedirect('/port/list/')
        else:
            response = HttpResponse(content_type='application/json')
            response.status_code = 401
            return response
    except Port.DoesNotExist:
        response = HttpResponse(content_type='application/json')
        response.status_code = 404
        return response

####### TRUCKER OFFER ########
def createTruckerOffer(request):
    if not request.user.is_authenticated():
        return redirect('/login/')
    if request.user.role == 'AD':
        ports = Port.objects.all()
        truckers = Trucker.objects.all()
        if request.method == 'POST':
            port_1 = Port.objects.get(pk=request.POST.get('port_1', None))
            port_2 = Port.objects.get(pk=request.POST.get('port_2', None))
            trucker = Trucker.objects.get(pk=request.POST.get('trucker', None))
            special_requirements = request.POST.get('special_requirements', None)
            other_notes = request.POST.get('other_notes', None)
            price = request.POST.get('price', None)

            trucker_offer = TruckerOffer(port_1=port_1, port_2=port_2, trucker=trucker,
            special_requirements=special_requirements, other_notes=other_notes, price=price)
            trucker_offer.save()

        return render(request, 'trucker_offer_add.html', {'ports': ports, 'truckers': truckers})
    else:
        return redirect('/')

def listTruckerOffer(request):
    if not request.user.is_authenticated():
        return redirect('/login/')

    trucker_offers = TruckerOffer.objects.all()
    return render(request, 'trucker_offer_list.html', {'trucker_offers': trucker_offers})

def getTruckerOffer(request, pk):
    if not request.user.is_authenticated():
        return redirect('/login/')

    trucker_offer = TruckerOffer.objects.get(pk=pk)
    return render(request, 'trucker_offer_detail.html', {'trucker_offer': trucker_offer})

def deleteTruckerOffer(request, pk):
    if not request.user.is_authenticated():
        return redirect('/login/')
    try:
        if request.user.role == 'AD':
            trucker_offer = TruckerOffer.objects.get(pk=pk)
            trucker_offer.delete()
            return HttpResponseRedirect('/trucker_offers/list/')
        else:
            response = HttpResponse(content_type='application/json')
            response.status_code = 401
            return response
    except TruckerOffer.DoesNotExist:
        response = HttpResponse(content_type='application/json')
        response.status_code = 404
        return response

####### Rate Request #########

def getAIFRateRequest(request):
    if not request.user.is_authenticated():
        return redirect('/login/')
    # if request.user.role == 'SA':
    #     return render(request, 'sales_rate_request_aif.html')
    if request.user.role == 'AD' or request.user.role == 'SA':
        clients = Client.objects.all()
        shipping_lines = ShippingLine.objects.all()
        return render(request, 'admin_rate_request_aif.html', {'clients': clients,
        'shipping_lines': shipping_lines})
    else:
        return redirect('/')

def getIFCLRateRequest(request):
    if not request.user.is_authenticated():
        return redirect('/login/')
    # if request.user.role == 'SA':
    #     return render(request, 'sales_rate_request_fcl.html')
    if request.user.role == 'AD' or request.user.role == 'SA':
        clients = Client.objects.all()
        shipping_lines = ShippingLine.objects.all()
        return render(request, 'admin_rate_request_fcl.html',{'clients': clients,
        'shipping_lines': shipping_lines, 'type':'IFCL'})
    else:
        return redirect('/')

def getXFCLRateRequest(request):
    if not request.user.is_authenticated():
        return redirect('/login/')
    # if request.user.role == 'SA':
    #     return render(request, 'sales_rate_request_fcl.html')
    if request.user.role == 'AD' or request.user.role == 'SA':
        clients = Client.objects.all()
        shipping_lines = ShippingLine.objects.all()
        return render(request, 'admin_rate_request_fcl.html',{'clients': clients,
        'shipping_lines': shipping_lines, 'type':'XFCL'})
    else:
        return redirect('/')

def getLCLRateRequest(request):
    if not request.user.is_authenticated():
        return redirect('/login/')
    # if request.user.role == 'SA':
    #     return render(request, 'sales_rate_request_lcl.html')
    if request.user.role == 'AD' or request.user.role == 'SA':
        clients = Client.objects.all()
        return render(request, 'admin_rate_request_lcl.html',{'clients': clients})
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

    # name = request.POST.get('client_name', None)
    # company_name = request.POST.get('company_name', None)
    # contact = request.POST.get('contact', None)
    # phone = request.POST.get('phone', None)
    # email = request.POST.get('email', None)
    # extra_information = request.POST.get('extra_info', None)
    # client = Client(name=name, company_name=company_name, contact=contact, phone=phone, email=email, extra_information=extra_information)
    # client.save()

    port_loading = request.POST.get('port_of_loading', None)
    port_discharge = request.POST.get('port_of_discharge', None)
    receipt_place = request.POST.get('receipt_place', None)
    # destination = Destination(port_of_loading=port_of_loading, loading_location_type=loading_location_type, port_of_discharge=port_of_discharge, discharge_location_type=discharge_location_type)
    # destination.save()

    address = request.POST.get('address', None)
    contact_person = request.POST.get('contact_person', None)
    contact_person_extra = request.POST.get('contact_person_extra', None)
    final_delivery_destination = FinalDeliveryDestination(address=address, contact_person=contact_person, contact_person_extra=contact_person_extra)
    final_delivery_destination.save()


    hazardous = request.POST.get('hazardous', None)
    non_hazardous = request.POST.get('non_hazardous', None)
    imo_class = IMOClass(hazardous=hazardous, non_hazardous=non_hazardous)
    imo_class.save()


    shipping_terms = request.POST.get('shipping_terms', None)
    shipment_term = request.POST.get('shipment_term', None)
    special_instructions = request.POST.get('special_instructions', None)

    if type == 'AIF':
        quantity = request.POST.get('quantity', None)
        commodity = request.POST.get('commodity', None)
        gross_weight = request.POST.get('gross_weight', None)
        pieces = request.POST.get('pieces', None)
        packing = request.POST.get('packing', None)
        weight_per_piece = request.POST.get('weight_per_piece', None)
        length = request.POST.get('length', None)
        width = request.POST.get('width', None)
        height = request.POST.get('height', None)
        chargeable_weight = request.POST.get('chargeable_weight', None)
        aif_cargo_details = AIFCargoSales(quantity=quantity, commodity=commodity,
        gross_weight=gross_weight, pieces=pieces, packing=packing, weight_per_piece=weight_per_piece,
        length=length, width=width, height=height, chargeable_weight=chargeable_weight)
        aif_cargo_details.save()

        if request.POST.get('preferred_shipping_line'):
            preferred_shipping_line = ShippingLine.objects.get(pk=request.POST.get('preferred_shipping_line', None))
        else:
            preferred_shipping_line = None
        if request.POST.get('other_shipping_line'):
            other_shipping_line = ShippingLine.objects.get(pk=request.POST.get('other_shipping_line', None))
        else:
            other_shipping_line = None

        rate_request = RateRequest(sales_person=sales_person, type=type,
        client=client, port_loading = port_loading,
        port_discharge = port_discharge, receipt_place=receipt_place,
        final_delivery_destination=final_delivery_destination,
        imo_class=imo_class, preferred_shipping_line=preferred_shipping_line,
        other_shipping_line=other_shipping_line, aif_cargo_details=aif_cargo_details,
        special_instructions=special_instructions, shipment_term=shipment_term,
        shipping_terms=shipping_terms)
        rate_request.save()

    elif type == 'IFCL':
        container_type = request.POST.get('container_type', None)
        special_equipment = request.POST.get('special_equipment', None)
        quantity = request.POST.get('quantity', None)
        commodity = request.POST.get('commodity', None)
        gross_weight = request.POST.get('gross_weight', None)
        tare_weight = request.POST.get('tare_weight', None)
        fcl_cargo_details = FCLCargoSales(container_type=container_type, special_equipment=special_equipment,
         quantity=quantity, commodity=commodity, gross_weight=gross_weight, tare_weight=tare_weight)
        fcl_cargo_details.save()


        preferred_shipping_line = ShippingLine.objects.get(pk=request.POST.get('preferred_shipping_line', None))
        other_shipping_line = ShippingLine.objects.get(pk=request.POST.get('other_shipping_line', None))

        rate_request = RateRequest(sales_person=sales_person, type=type,
         client=client,  port_loading = port_loading,
         port_discharge = port_discharge, receipt_place=receipt_place, final_delivery_destination=final_delivery_destination,
          imo_class=imo_class,
          fcl_cargo_details=fcl_cargo_details, preferred_shipping_line=preferred_shipping_line,
          other_shipping_line=other_shipping_line, shipping_terms=shipping_terms,
          special_instructions=special_instructions, shipment_term=shipment_term)
        rate_request.save()

    elif type == 'XFCL':
        container_type = request.POST.get('container_type', None)
        special_equipment = request.POST.get('special_equipment', None)
        quantity = request.POST.get('quantity', None)
        commodity = request.POST.get('commodity', None)
        fcl_cargo_details = FCLCargoSales(container_type=container_type, special_equipment=special_equipment,
         quantity=quantity, commodity=commodity)
        fcl_cargo_details.save()


        preferred_shipping_line = ShippingLine.objects.get(pk=request.POST.get('preferred_shipping_line', None))
        other_shipping_line = ShippingLine.objects.get(pk=request.POST.get('other_shipping_line', None))

        rate_request = RateRequest(sales_person=sales_person, type=type,
         client=client,  port_loading = port_loading,
         port_discharge = port_discharge, receipt_place=receipt_place,final_delivery_destination=final_delivery_destination,
          imo_class=imo_class,
          fcl_cargo_details=fcl_cargo_details, preferred_shipping_line=preferred_shipping_line,
          other_shipping_line=other_shipping_line, shipping_terms=shipping_terms,
          special_instructions=special_instructions, shipment_term=shipment_term)
        rate_request.save()

    else:
        quantity = request.POST.get('quantity', None)
        commodity = request.POST.get('commodity', None)
        gross_weight = request.POST.get('gross_weight', None)
        pieces = request.POST.get('pieces', None)
        packing = request.POST.get('packing', None)
        weight_per_piece = request.POST.get('weight_per_piece', None)
        length = request.POST.get('length', None)
        width = request.POST.get('width', None)
        height = request.POST.get('height', None)
        total_volume = request.POST.get('total_volume', None)
        lcl_cargo_details = LCLCargoSales(quantity=quantity, commodity=commodity,
        gross_weight=gross_weight, pieces=pieces, packing=packing, weight_per_piece=weight_per_piece,
        length=length, width=width, height=height, total_volume=total_volume)
        lcl_cargo_details.save()

        rate_request = RateRequest(sales_person=sales_person, type=type,
        client=client, final_delivery_destination=final_delivery_destination,imo_class=imo_class,
        lcl_cargo_details=lcl_cargo_details, shipping_terms=shipping_terms, special_instructions=special_instructions
        , shipment_term=shipment_term, port_loading = port_loading,
        port_discharge = port_discharge, receipt_place=receipt_place,)
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
            elif rate_request.type == 'IFCL':
                return render(request, 'admin_rate_request_fcl_view.html', { 'rate_request': rate_request, 'type': 'IFCL'})
            elif rate_request.type == 'XFCL':
                return render(request, 'admin_rate_request_fcl_view.html', { 'rate_request': rate_request, 'type': 'XFCL' })
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
            ports = Port.objects.all()
            return render(request, 'admin_offer_air.html', { 'quotation': quotation, 'ports': ports })
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
            return render(request, 'admin_offer_sea.html', { 'quotation': quotation ,'shipping_lines': shipping_lines, 'type': quotation.rate_request.type})
        else:
            return redirect('/')
    except RateRequest.DoesNotExist:
        return redirect('/404/')

def getFCLOffer(request, pk):
    if not request.user.is_authenticated():
        return redirect('/login/')
    try:
        quotation = Quotation.objects.get(pk=pk)
        if request.user.role == 'AD' or 'SA':
            shipping_lines = ShippingLine.objects.all()
            return render(request, 'admin_offer_fcl.html', { 'quotation': quotation ,'shipping_lines': shipping_lines, 'type': quotation.rate_request.type})
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
        rate_request = quotation.rate_request
    except Quotation.DoesNotExist:
        return redirect('/404/')

    client = quotation.client

    admins = User.objects.filter(role='AD')
    email_list = [];
    for admin in admins:
        email_list.append(admin.email)
    email_list.append(sales_person.email)

    terms = request.POST.get('terms', None)
    if type == 'A':
        air_freight_kg = request.POST.get('air_freight_kg', None)
        fuel_sur_charge_kg = request.POST.get('fuel_sur_charge_kg', None)
        security_fees_kg = request.POST.get('security_fees_kg', None)
        exw_charges = request.POST.get('exw_charges', None)
        screening_fees = request.POST.get('screening_fees', None)
        storage = request.POST.get('storage', None)
        inland = request.POST.get('inland_selling', None)
        packing = request.POST.get('packing', None)
        taxes_duties = request.POST.get('taxes_duties', None)
        handling_fees = request.POST.get('handling_fees', None)
        official_receipts = request.POST.get('official_receipts', None)
        p_share = request.POST.get('p_share', None)
        other_notes = request.POST.get('other_notes', None)
        offer_validity = request.POST.get('offer_validity', None)
        air_quotation = AirQuotation(air_freight_kg=air_freight_kg, fuel_sur_charge_kg=fuel_sur_charge_kg, security_fees_kg=security_fees_kg, exw_charges=exw_charges, screening_fees=screening_fees, storage=storage, inland=inland, packing=packing, taxes_duties=taxes_duties, handling_fees=handling_fees, official_receipts=official_receipts, p_share=p_share, other_notes=other_notes, offer_validity=offer_validity)
        air_quotation.save()

        offer = Offer(quotation=quotation, type=type, sales_person=sales_person, client=client, air_quotation=air_quotation, terms=terms)
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

    elif type == 'S':
        shipping_line = ShippingLine.objects.get(pk=request.POST.get('shipping_line', None))
        ocean_freight = request.POST.get('ocean_freight', None)
        thc = request.POST.get('thc', None)
        transportation = request.POST.get('transportation', None)
        transfer = request.POST.get('transfer', None)
        clearance_pol_selling = request.POST.get('clearance_pol_selling', None)
        clearance_pod_selling = request.POST.get('clearance_pod_selling', None)
        bl_fees = request.POST.get('bl_fees', None)
        telex_release = request.POST.get('telex_release', None)
        # free_time_at_destination = request.POST.get('free_time_at_destination', None)
        # vessels = request.POST.get('vessels', None)
        payment_credit = request.POST.get('payment_credit', None)
        # official_receipts = request.POST.get('official_receipts', None)
        other_notes = request.POST.get('other_notes', None)
        # offer_validity = request.POST.get('offer_validity', None)
        sea_quotation = SeaQuotation(shipping_line=shipping_line,
        ocean_freight=ocean_freight, thc=thc, transportation=transportation,
        transfer=transfer, clearance_pol_selling=clearance_pol_selling, clearance_pod_selling=clearance_pod_selling, bl_fees=bl_fees, telex_release=telex_release,
         payment_credit=payment_credit, other_notes=other_notes)
        sea_quotation.save()

        offer = Offer(quotation=quotation, type=type, sales_person=sales_person,
         client=client, sea_quotation=sea_quotation, terms=terms)
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
    else:
        ocean_freight = request.POST.get('ocean_freight', None)
        pre_carriage = request.POST.get('pre_carriage', None)
        thc_origin = request.POST.get('thc_origin', None)
        custom_clearance_origin = request.POST.get('custom_clearance_origin', None)
        documentation_origin = request.POST.get('documentation_origin', None)
        xray = request.POST.get('xray', None)
        baf = request.POST.get('baf', None)
        caf = request.POST.get('caf', None)
        others_origin = request.POST.get('others_origin', None)
        documentation_destination = request.POST.get('documentation_destination', None)
        thc_destination = request.POST.get('thc_destination', None)
        storage = request.POST.get('storage', None)
        demurrage = request.POST.get('demurrage', None)
        custom_clearance_destination = request.POST.get('custom_clearance_destination', None)
        on_carriage = request.POST.get('on_carriage', None)
        others_destination = request.POST.get('others_destination', None)
        official_receipts_selling = request.POST.get('official_receipts_selling', None)
        if type == 'IFCL':
            road_cartage = request.POST.get('road_cartage', None)
            documentation_origin = request.POST.get('documentation_origin', None)

            fcl_sea_quotation = FCLSeaQuotation(
            ocean_freight=ocean_freight,
            pre_carriage=pre_carriage,
            thc_origin=thc_origin, custom_clearance_origin=custom_clearance_origin,
            documentation_origin=documentation_origin,
            xray=xray,
            baf=baf, caf=caf,
            others_origin=others_origin,
            documentation_destination=documentation_destination,
            thc_destination=thc_destination,
            storage=storage,
            demurrage=demurrage,
            custom_clearance_destination=custom_clearance_destination,
            road_cartage=road_cartage,
            official_receipts_selling=official_receipts_selling,
            on_carriage=on_carriage, others_destination=others_destination)
        elif type == 'XFCL':
            container_fees = request.POST.get('container_fees', None)
            delay = request.POST.get('delay', None)
            fcl_sea_quotation = FCLSeaQuotation(
            ocean_freight=ocean_freight,
            pre_carriage=pre_carriage,
            thc_origin=thc_origin, custom_clearance_origin=custom_clearance_origin,
            xray=xray,
            baf=baf, caf=caf,
            others_origin=others_origin,
            documentation_destination=documentation_destination,
            thc_destination=thc_destination,
            storage=storage,
            demurrage=demurrage,
            custom_clearance_destination=custom_clearance_destination,
            official_receipts_selling=official_receipts_selling,
            on_carriage=on_carriage, others_destination=others_destination,
            container_fees=container_fees, delay=delay)

        fcl_sea_quotation.save()
        offer = Offer(quotation=quotation, type='S', sales_person=sales_person,
         client=client, fcl_quotation=fcl_sea_quotation, terms=terms)
        offer.save()

        # msg_plain = render_to_string('./offerFCLSeaEmail.txt', {'offer': offer})
        # msg_html = render_to_string('./offerFCLSeaEmail.html', {'offer': offer})
        # send_mail(
        #     "Master Freight Offer",
        #     msg_plain,
        #     request.user.email,
        #     email_list,
        #     html_message=msg_html,
        #     fail_silently=False,
        # )
    # elif type == 'XFCL':

    if offer:
        quotation.status = 'OC'
        rate_request.status = 'OS'
        quotation.save()
        rate_request.save()

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
            offer.save()

            rate_request = offer.quotation.rate_request
            print "rate request"
            print rate_request
            if request.POST.get('status', offer.status) == 'A':
                offer.quotation.status = 'OA'
                rate_request.status = 'OA'
            elif request.POST.get('status', offer.status) == 'D':
                offer.quotation.status = 'DO'
                rate_request.status = 'DO'
            elif request.POST.get('status', offer.status) == 'R':
                offer.quotation.status = 'OR'
                rate_request.status = 'OR'
            rate_request.save()
            offer.quotation.save()
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
                if offer.quotation.type == 'IFCL' or offer.quotation.type == 'XFCL':
                    return render(request, 'admin_offer_fcl_view.html', { 'offer': offer , 'eligible': eligible})
                else:
                    return render(request, 'admin_offer_sea_view.html', { 'offer': offer , 'eligible': eligible})
        elif request.user.role == 'AC' and offer.status == 'A':
            eligible = False
            if offer.type == 'A':
                return render(request, 'admin_offer_air_view.html', { 'offer': offer,  'eligible': eligible })
            elif offer.type == 'S':
                if offer.quotation.type == 'IFCL' or offer.quotation.type == 'XFCL':
                    return render(request, 'admin_offer_fcl_view.html', { 'offer': offer , 'eligible': eligible})
                else:
                    return render(request, 'admin_offer_sea_view.html', { 'offer': offer , 'eligible': eligible})
        else:
            return redirect('/')
    except Offer.DoesNotExist:
        return redirect('/404/')

def viewOfferClientFormat(request, pk):
    if not request.user.is_authenticated():
        return redirect('/login/')
    try:
        offer = Offer.objects.get(pk=pk)
        print offer.reference
        if request.user.role == 'AD' or (request.user.role == 'SA' and offer.sales_person.id == request.user.id):
            eligible = True
            if offer.type == 'A':
                return render(request, 'admin_offer_client_air_view.html', { 'offer': offer,  'eligible': eligible })
            elif offer.type == 'S':
                if offer.quotation.type == 'IFCL' or offer.quotation.type == 'XFCL':
                    return render(request, 'admin_offer_client_fcl_view.html', { 'offer': offer , 'eligible': eligible})
                else:
                    return render(request, 'admin_offer_client_sea_view.html', { 'offer': offer , 'eligible': eligible})

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
def portSelectHandler(request):
    port_id = request.GET["id"]
    port = Port.objects.get(pk=port_id)
    trucker_offers_port1 = TruckerOffer.objects.filter(port_1=port)
    trucker_offers_port2 = TruckerOffer.objects.filter(port_2=port)
    trucker_offers = list(trucker_offers_port1) + list(trucker_offers_port2)
    formated_offers = []
    for trucker_offer in trucker_offers:
        data = {'id' : trucker_offer.pk, 'port_1': trucker_offer.port_1.name, 'port_2': trucker_offer.port_2.name, 'trucker': trucker_offer.trucker.company_name, 'price': trucker_offer.price}
        formated_offers.append(data)
    print formated_offers
    return JsonResponse(formated_offers, safe=False)

def truckerOfferSelectHandler(request):
   offer_id = request.GET["id"]
   trucker_offer = TruckerOffer.objects.get(pk=offer_id)
   return JsonResponse({'trucker_offer_id': trucker_offer.id, 'trucker_offer_price': trucker_offer.price})
######### Quotation ##############

def getAIFQuotation(request, pk):
    if not request.user.is_authenticated():
        return redirect('/login/')
    try:
        rate_request = RateRequest.objects.get(pk=pk)
        ports = Port.objects.all()
        if request.user.role == 'OP' or request.user.role == 'AD':
            return render(request, 'admin_quotations_aif.html', { 'rate_request': rate_request, 'ports': ports })
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
             'shipping_lines': shipping_lines, 'type': rate_request.type })
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

    if request.POST.get('shipping_line'):
        shipping_line = ShippingLine.objects.get(pk=request.POST.get('shipping_line', None))
    else:
        shipping_line = None


    special_instructions = request.POST.get('special_instructions', None)

    if type == 'AIF':
        num_of_packages = request.POST.get('no_of_packages', None)
        actual_weight = request.POST.get('actual_weight', None)
        transit_time = request.POST.get('transit_date', None)
        route = request.POST.get('route', None)
        arrival_date = request.POST.get('arrival_date', None)
        mawb_number = request.POST.get('mawb', None)
        hawb_number = request.POST.get('hawb', None)

        aif_cargo_details = AIFCargoOperations(num_of_packages=num_of_packages,
        actual_weight=actual_weight, transit_time=transit_time, route=route,
        mawb_number=mawb_number, hawb_number=hawb_number)
        aif_cargo_details.save()

        air_freight_kg_net = request.POST.get('airfreight_net', None)
        fuel_sur_charge_kg_net = request.POST.get('fuel_surcharge_net', None)
        security_fees_kg_net = request.POST.get('security_fees_net', None)
        exw_charges_net = request.POST.get('exw_charges_net', None)
        screening_fees_net = request.POST.get('screening_fees_net', None)
        storage_net = request.POST.get('storage_net', None)
        if request.POST.get('inland_net'):
            inland_net = TruckerOffer.objects.get(pk=request.POST.get('inland_net', None))
        else:
            inland_net = None
        packing_net = request.POST.get('packing_net', None)
        taxes_duties_net = request.POST.get('taxes_n_duties_net', None)
        handling_fees_net = request.POST.get('handling_fees_net', None)
        p_share_net = request.POST.get('p_share_net', None)

        aif_quotation = AIFQuotation(air_freight_kg_net=air_freight_kg_net,
          fuel_sur_charge_kg_net=fuel_sur_charge_kg_net,
          security_fees_kg_net=security_fees_kg_net,
          exw_charges_net=exw_charges_net,
          screening_fees_net=screening_fees_net,
          storage_net=storage_net,
          inland_net=inland_net,
          packing_net=packing_net,
          taxes_duties_net=taxes_duties_net,
          handling_fees_net=handling_fees_net,
          p_share_net=p_share_net)
        aif_quotation.save()

        quotation = Quotation(arrival_date=arrival_date, departure_date=departure_date,
        rate_request=rate_request, sales_person=sales_person,
         operations_person=operations_person, type=type, client=client,
         aif_cargo_details=aif_cargo_details, aif_quotation=aif_quotation, special_instructions=special_instructions)
        quotation.save()

    elif type == 'IFCL':
        agent_details = request.POST.get('agent_details', None)

        fcl_cargo_details = FCLCargoOperations(shipping_line=shipping_line)
        fcl_cargo_details.save()

        ocean_freight = request.POST.get('ocean_freight', None)
        thc_origin = request.POST.get('thc_origin', None)
        pre_carriage = request.POST.get('pre_carriage', None)
        custom_clearance_origin = request.POST.get('custom_clearance_origin', None)
        documentation_origin = request.POST.get('documentation_origin', None)
        baf = request.POST.get('baf', None)
        caf = request.POST.get('caf', None)
        others_origin = request.POST.get('others_origin', None)
        xray = request.POST.get('xray', None)

        documentation_destination = request.POST.get('documentation_destination', None)
        thc_destination = request.POST.get('thc_destination', None)
        storage = request.POST.get('storage', None)
        demurrage = request.POST.get('demurrage', None)
        custom_clearance_destination = request.POST.get('custom_clearance_destination', None)
        road_cartage = request.POST.get('baf', None)
        on_carriage = request.POST.get('caf', None)
        others_destination = request.POST.get('others_destination', None)

        official_receipts_net = request.POST.get('official_receipts_net', None)

        fcl_quotation = FCLQuotation(
        ocean_freight=ocean_freight,
        pre_carriage=pre_carriage,
        thc_origin=thc_origin, custom_clearance_origin=custom_clearance_origin,
        documentation_origin=documentation_origin,
        xray=xray,
        baf=baf, caf=caf,
        others_origin=others_origin,
        documentation_destination=documentation_destination,
        thc_destination=thc_destination,
        storage=storage,
        demurrage=demurrage,
        custom_clearance_destination=custom_clearance_destination,
        road_cartage=road_cartage,
        official_receipts_net=official_receipts_net,
        on_carriage=on_carriage, others_destination=others_destination)
        fcl_quotation.save()

        free_time_at_destination = request.POST.get('free_time_at_destination', None)
        vessels_available = request.POST.get('vessels_available', None)
        route = request.POST.get('route', None)
        transit_time = request.POST.get('transit_time', None)
        offer_validity = request.POST.get('offer_validity', None)
        extra_notes = ExtraNotes(free_time_at_destination=free_time_at_destination,
        vessels_available=vessels_available, route=route, transit_time=transit_time, offer_validity=offer_validity)
        extra_notes.save()

        quotation = Quotation(arrival_date=arrival_date, departure_date=departure_date,
         rate_request=rate_request, sales_person=sales_person, operations_person=operations_person,
          type=type, client=client, special_instructions=special_instructions,
           agent_details=agent_details, fcl_cargo_details=fcl_cargo_details,
            fcl_quotation=fcl_quotation, extra_notes=extra_notes)
        quotation.save()
    elif type == 'XFCL':
        agent_details = request.POST.get('agent_details', None)
        fcl_cargo_details = FCLCargoOperations(shipping_line=shipping_line)
        fcl_cargo_details.save()


        xray = request.POST.get('xray', None)
        ocean_freight = request.POST.get('ocean_freight', None)
        thc_origin = request.POST.get('thc_origin', None)
        pre_carriage = request.POST.get('pre_carriage', None)
        custom_clearance_origin = request.POST.get('custom_clearance_origin', None)
        documentation_origin = request.POST.get('documentation_origin', None)
        baf = request.POST.get('baf', None)
        caf = request.POST.get('caf', None)
        others_origin = request.POST.get('others_origin', None)
        container_fees = request.POST.get('container_fees', None)
        delay = request.POST.get('delay', None)
        documentation_destination = request.POST.get('documentation_destination', None)
        thc_destination = request.POST.get('thc_destination', None)
        storage = request.POST.get('storage', None)
        demurrage = request.POST.get('demurrage', None)
        custom_clearance_destination = request.POST.get('custom_clearance_destination', None)
        road_cartage = request.POST.get('baf', None)
        on_carriage = request.POST.get('caf', None)
        others_destination = request.POST.get('others_destination', None)

        official_receipts_net = request.POST.get('official_receipts_net', None)

        fcl_quotation = FCLQuotation(
        ocean_freight=ocean_freight,
        pre_carriage=pre_carriage,
        thc_origin=thc_origin, custom_clearance_origin=custom_clearance_origin,
        documentation_origin=documentation_origin,
        xray=xray,
        baf=baf, caf=caf,
        others_origin=others_origin,
        documentation_destination=documentation_destination,
        thc_destination=thc_destination,
        storage=storage,
        demurrage=demurrage,
        custom_clearance_destination=custom_clearance_destination,
        road_cartage=road_cartage,
        on_carriage=on_carriage, others_destination=others_destination,
        official_receipts_net=official_receipts_net,
        container_fees=container_fees,
        delay=delay)
        fcl_quotation.save()

        free_time_at_destination = request.POST.get('free_time_at_destination', None)
        vessels_available = request.POST.get('vessels_available', None)
        route = request.POST.get('route', None)
        transit_time = request.POST.get('transit_time', None)
        offer_validity = request.POST.get('offer_validity', None)
        extra_notes = ExtraNotes(free_time_at_destination=free_time_at_destination, vessels_available=vessels_available, route=route, transit_time=transit_time, offer_validity=offer_validity)
        extra_notes.save()

        quotation = Quotation(arrival_date=arrival_date, departure_date=departure_date,
        rate_request=rate_request, sales_person=sales_person, operations_person=operations_person, type=type,
        client=client, special_instructions=special_instructions, agent_details=agent_details, fcl_cargo_details=fcl_cargo_details, fcl_quotation=fcl_quotation, extra_notes=extra_notes)
        quotation.save()

    else:
        agent_details = request.POST.get('agent_details', None)
        co_loader = request.POST.get('co_loader', None)

        container_type = request.POST.get('container_type', None)
        num_of_packages = request.POST.get('number_of_packages', None)
        lcl_cargo_details = LCLCargoOperations(shipping_line=shipping_line,
        container_type=container_type, num_of_packages=num_of_packages)
        lcl_cargo_details.save()

        ocean_freight_net = request.POST.get('ocean_freight_net', None)
        thc_net = request.POST.get('thc_net', None)
        transportation_net = request.POST.get('transportation_net', None)
        transfer_net = request.POST.get('transfer_net', None)
        clearance_pol_net = request.POST.get('clearance_pol_net', None)
        clearance_pod_net = request.POST.get('clearance_pod_net', None)
        bl_fees_net = request.POST.get('bl_fees_net', None)
        telex_release_net = request.POST.get('telex_release_net', None)
        ex_work_net = request.POST.get('ex_work_net', None)
        official_receipts_net = request.POST.get('official_receipts_net', None)
        lcl_quotation = LCLQuotation(
        ocean_freight_net=ocean_freight_net,
        thc_net=thc_net,
        transportation_net=transportation_net,
        transfer_net=transfer_net,
        clearance_pol_net=clearance_pol_net,
        clearance_pod_net=clearance_pod_net,
        bl_fees_net=bl_fees_net,
        telex_release_net=telex_release_net,
        ex_work_net=ex_work_net,
        official_receipts_net=official_receipts_net)
        lcl_quotation.save()

        free_time_at_destination = request.POST.get('free_time_at_destination', None)
        vessels_available = request.POST.get('vessels_available', None)
        route = request.POST.get('route', None)
        transit_time = request.POST.get('transit_time', None)
        offer_validity = request.POST.get('offer_validity', None)
        extra_notes = ExtraNotes(free_time_at_destination=free_time_at_destination, vessels_available=vessels_available, route=route, transit_time=transit_time, offer_validity=offer_validity)
        extra_notes.save()

        quotation = Quotation(arrival_date=arrival_date, departure_date=departure_date,
        rate_request=rate_request, sales_person=sales_person, operations_person=operations_person,
        type=type, client=client, special_instructions=special_instructions,
        agent_details=agent_details, co_loader=co_loader, lcl_cargo_details=lcl_cargo_details,
        lcl_quotation=lcl_quotation, extra_notes=extra_notes)
        quotation.save()

    if quotation:
        rate_request.status = 'QR'
        rate_request.save()

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
        offer_accepted = False;
        has_offer = False;
        if quotation.offers.all():
            has_offer = True

        print quotation.offers.all()
        print has_offer
        for offer in quotation.offers.all():
            if offer.status == 'A':
                offer_accepted = offer_accepted or True
            else:
                offer_accepted = offer_accepted or False
        if request.user.role == 'AD' or request.user.role == 'SA' or request.user.role == 'OP' or (request.user.role == 'AC' and quotation.offers.first().status == 'A'):
            if quotation.type == 'AIF':
                return render(request, 'admin_quotations_aif_view.html', { 'quotation': quotation, 'offer_accepted': offer_accepted, 'has_offer': has_offer })
            elif quotation.type == 'IFCL' or quotation.type == 'XFCL':
                return render(request, 'admin_quotations_fcl_view.html', { 'quotation': quotation, 'offer_accepted': offer_accepted, 'has_offer': has_offer })
            elif quotation.type == 'LCL':
                return render(request, 'admin_quotations_lcl_view.html', { 'quotation': quotation, 'offer_accepted': offer_accepted, 'has_offer': has_offer})
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
