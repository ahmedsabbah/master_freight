from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from authentication.models import User

def login_user(request):
    if request.user.is_authenticated():
        return redirect('/')
    if request.method == 'POST':
        message = ''
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        if email and password:
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                message = 'Invalid email or password'
                return render(request, 'login.html', {'message': message, 'email': email})
        else:
            message = 'Missing email or password'
            return render(request, 'login.html', {'message': message, 'email': email})
    else:
        return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/login/')
