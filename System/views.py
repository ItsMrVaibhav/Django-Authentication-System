from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from System.forms import UserForm
from django.contrib.auth import login, logout, authenticate

def home(request):
    return render(request, "index.html", context = None)

def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"{username}, account successfully created!")
            login(request, user)

            return render(request, "index.html")
        else:
            for message in form.error_messages:
                messages.error(request, f"{message}")

    return render(request, "register.html", context = None)

def loginUser(request):
    return render(request, "login.html", context = None)

def loginOut(request):
    return render(request, "login.html", context = None)

def profile(request):
    return render(request, "profile.html", context = None)
