from django import views
from django.urls import path
from .views import *






urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('pricing/', pricing, name='pricing'),
    path('contact/', contact, name='contact'),
    path('success/', success_view, name='success_view'),
    path('create_appointment/', create_appointment, name='create_appointment'),
    
    
    
   
]