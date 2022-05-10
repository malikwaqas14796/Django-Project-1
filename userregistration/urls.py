from django.contrib import admin
from django.urls import path 
from userregistration import views

urlpatterns = [
    path('createuser', views.createuser, name = 'createuser'),
    path('getusers', views.getusers, name = 'getusers')
]