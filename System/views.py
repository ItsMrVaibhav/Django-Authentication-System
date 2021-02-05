from django.shortcuts import render

def home(request):
    return render(request, "index.html", context = None)

def register(request):
    return render(request, "register.html", context = None)

def login(request):
    return render(request, "login.html", context = None)
