from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.conf import settings
from django.core.mail import send_mail

def login(request):
    return render(request,"login/login.html") 

def process_login(request):
    if request.method == 'POST':
        username = request.POST['userName']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if (request.user.is_authenticated):
                return redirect('store')
        else:
            return redirect('login')

def register(request):
    return render(request,"login/register.html")

def process_regis(request):
    if request.method == "POST":
        username = request.POST["userName"]
        password = request.POST["password"]
        email = request.POST["email"]

        user = User.objects.create_user(
            username = username,
            password = password,
            email = email
        )
        user.save()
        subject = 'welcome to SA Store'
        message = f'Hi {user.username}, thank you for registering in geeksforgeeks.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email, ]
        send_mail( subject, message, email_from, recipient_list )
        return redirect('login')
    return render(request,"login/register.html") 


def logout(request):
    auth.logout(request)
    return render(request,"login/login.html") 