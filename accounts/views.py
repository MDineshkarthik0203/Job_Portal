from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.contrib.auth.models import User

def register_page(request):
    if request.method == "POST":
        user = User.objects.create_user(
            username=request.POST.get('username'),
            email=request.POST.get('email'),
            password=request.POST.get('password'),
        )

        user.role = request.POST.get('role')
        user.save()

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