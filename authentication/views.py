from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from authentication.models import User, Token
from django.core.mail import send_mail

def loginUser(request):
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

def logoutUser(request):
    logout(request)
    return redirect('/login/')

def resetPassword(request, token):
    try:
        token = Token.objects.get(token=token)
        if (request.method == 'POST'):
            new_password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            if new_password and confirm_password and (new_password==confirm_password):
                user = token.user
                user.set_password(new_password)
                user.save()
                return redirect('/login/')
            else:
                return render(request, 'reset_password.html', {'message': "Passwords don't match"})
        else:
            return render(request, 'reset_password.html', {'token': token})
    except Token.DoesNotExist:
        return redirect('/')

def forgotPassword(request):
    if request.method == 'POST':
        try:
            email = request.POST.get('email', None)
            if email:
                user = User.objects.get(email=email)
                message = 'An email was sent to you.'
                try:
                    token = Token.objects.get(user=user)
                    # send_mail(
                    #     'Master Freight Password Reset',
                    #     'Click on the following link to reset your password http://localhost:8000/password_reset/%s' % token.token,
                    #     'info@isparkegypt.com',
                    #     ['%s' % user.email],
                    #     fail_silently=False,
                    # )
                except Token.DoesNotExist:
                    token = Token(user=user)
                    token.save()
                    # send_mail(
                    #     'Master Freight Password Reset',
                    #     'Click on the following link to reset your password http://localhost:8000/password_reset/%s' % token.token,
                    #     'info@isparkegypt.com',
                    #     ['%s' % user.email],
                    #     fail_silently=False,
                    # )
            else:
                message = 'Enter a valid email.'
        except User.DoesNotExist:
            message = 'You are not registered.'
        return render(request, 'forgot_password.html', {'message': message})
    else:
        return render(request, 'forgot_password.html')

def addUser(request):
    if not request.user.is_authenticated():
        return redirect('/login/')
    if request.user.role != 'AD':
        return redirect('/')
    if request.method == 'GET':
        return render(request, 'add_user.html')
    else:
        email = request.POST.get('email', None)
        first_name = request.POST.get('first_name', None)
        last_name = request.POST.get('last_name', None)
        role = request.POST.get('role', None)
        password = request.POST.get('password', None)
        confirm_password = request.POST.get('confirm_password', None)
        if not role:
            return render(request, 'add_user.html', {'message': 'Missing role'})
        if not email:
            return render(request, 'add_user.html', {'message': 'Missing email'})
        if not first_name:
            return render(request, 'add_user.html', {'message': 'Missing first name'})
        if not last_name:
            return render(request, 'add_user.html', {'message': 'Missing last name'})
        if not password:
            return render(request, 'add_user.html', {'message': 'Missing password'})
        if not confirm_password:
            return render(request, 'add_user.html', {'message': 'Missing confirm password'})
        if password != confirm_password:
            return render(request, 'add_user.html', {'message': 'Passwords do not match'})
        user = User(role=role, email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        return render(request, 'add_user.html', {'message': 'User created'})

def viewUser(request, pk):
    if not request.user.is_authenticated():
        return redirect('/login/')
    if request.user.role != 'AD':
        return redirect('/')
    try:
        user = User.objects.get(pk=pk)
        return render(request, 'view_user.html', {'user': user})
    except User.DoesNotExist:
        return redirect('/users/')

def viewUsers(request, pk):
    if not request.user.is_authenticated():
        return redirect('/login/')
    if request.user.role != 'AD':
        return redirect('/')
    users = Users.objects.all()
    return render(request, 'view_users.html', {'users': users})

def removeUser(request, pk):
    if not request.user.is_authenticated():
        return redirect('/login/')
    if request.user.role != 'AD':
        return redirect('/')
    try:
        user = User.objects.get(pk=pk)
        user.delete()
        return redirect('/admin/employees')
    except User.DoesNotExist:
        return redirect('/admin/employees')
