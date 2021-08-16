from django.shortcuts import render, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

# Create your views here.

def index(request):
    if request.user.is_anonymous:
        return redirect("/signin") 
    return render(request, 'index.html')

def about(request):
    if request.user.is_anonymous:
        return redirect("/signin") 
    return render(request, 'about.html')

def contact(request):
    if request.user.is_anonymous:
        return redirect("/signin") 
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Successfully Submitted!')

    return render(request, 'contact.html')

def signin(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")

        else:
            # No backend authenticated the credentials
            return render(request, 'signin.html')
    return render(request, 'signin.html')

def signout(request):
    logout(request)
    return redirect("/signin")
