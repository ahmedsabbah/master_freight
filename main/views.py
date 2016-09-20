from django.shortcuts import render, redirect

def test(request):
    return render(request, 'quotations_lcl.html', {})

def home(request):
    return render(request, 'quotations_lcl.html')

def main(request):
    if not request.user.is_authenticated():
        return redirect('/login')
    if request.user.role == 'SA':
        return render(request, 'quotations_lcl.html')
    elif request.user.role == 'OP':
        return render(request, 'quotations_lcl.html')
    elif request.user.role == 'AC':
        return render(request, 'quotations_lcl.html')
    elif request.user.role == 'HR':
        return render(request, 'quotations_lcl.html')
    elif request.user.role == 'AD':
        return render(request, 'quotations_lcl.html')
    else:
        return render(request, '404.html')
