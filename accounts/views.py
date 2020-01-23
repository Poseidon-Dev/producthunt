from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        if request.POST['inputPassword1'] == request.POST['inputPassword2']:
            try:
                user = User.objects.get(username=request.POST['inputUsername'])
                return render(request, 'accounts/signup.html', {'error':'Username not available'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['inputUsername'], password=request.POST['inputPassword1'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Password did not match'})
    else:
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['inUser'], password=request.POST['inPass'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error':'Username or password invalid'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    else:
        return redirect('home')
    