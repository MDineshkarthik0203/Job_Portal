from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User

def register_page(request):
    if request.method == "POST":
        User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            password=request.POST['password'],
            role=request.POST['role']
        )
        return redirect('/login/')
    return render(request, 'register.html')


def login_page(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    
    # ✅ THIS LINE WAS MISSING
    return render(request, 'login.html')


def logout_page(request):
    logout(request)
    return redirect('/login/')