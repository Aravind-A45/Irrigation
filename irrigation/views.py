from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib import messages
# Create your views here.

def home(request):
  return render(request, "home.html")

def index(request):
  return render(request, "index.html")  

def notification(request):
  return render(request, "notification.html")

def information(request):
  return render(request, "information.html")

def contact(request):
  return render(request, "contact.html")      

def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return redirect('signup')
 
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')    

def signup(request):
    details = User.objects.all()

    if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            con_password = request.POST.get('con_password')

            if password == con_password:
              if User.objects.filter(username=username).exists():
                  messages.info(request, f"User with roll number {username} already exists.")
                  return redirect('signup')

              user = User.objects.create_user(username=username, password=password)
              user = authenticate(username=username, password=password)
              if user is not None:
                  return redirect('login')
              else:
                  messages.error(request, "Invalid username or password.")
            else:
              messages.info(request, f"Password and Confirm Password are not matching")   

    messages.success(request, f"Password should be 8 characters") 
    messages.success(request, f"Password should be mixed of Alpha Numerics and Spl Characters") 
    return render(request, 'signup.html')