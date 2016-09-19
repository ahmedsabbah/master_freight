from django.shortcuts import render

# Create your views here.
def test(request):
    return render(request, 'quotations_lcl.html', {})

def home(request):
    return render(request, 'quotations_lcl.html')

def jobs(request):
    if request.user.type == 'sales':
        return render(request, 'Quotations-LCL.html')
    elif request.user.type == 'operations':
        return render(request, 'Quotations-LCL.html')
    elif request.user.type == 'accounting':
        return render(request, 'Quotations-LCL.html')
    elif request.user.type == 'hr':
        return render(request, 'Quotations-LCL.html')
    elif request.user.type == 'admin':
        return render(request, 'Quotations-LCL.html')
    else:
        return render(request, '404.html')
