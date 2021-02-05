from django.contrib import admin
from django.urls import path, include
from System import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("login/", views.loginUser, name = "login"),
    path("register/", views.register, name = "register"),
    path("profile/", views.profile, name = "profile"),
]
