from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from .forms import AppointmentForm
from .models import *
from django.core.mail import send_mail
from datetime import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.utils.dateparse import parse_date, parse_time
from django.http import HttpResponseRedirect
from django.urls import reverse




# Create your views here.
def home(request):
    form = AppointmentForm()  # Create an instance of the form
    return render(request, 'index.html', {'form': form})

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def pricing(request):
    return render(request,'pricing.html')

def contact(request):
    return render(request,'contact.html')

def appointment(request):
    return render(request, 'appointment.html') 

def success_view(request):
    return render(request, 'success.html')   
   
def store(request):
    return render(request, 'store.html')




def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            # Log the form data
            print(form.cleaned_data)
            messages.success(request, 'Appointment created successfully.')
            return HttpResponseRedirect('/success/') 
        else:
            messages.error(request, 'Error submitting the form. Please check the entered data.')
    else:
        form = AppointmentForm()

    return render(request, 'index.html', {'form': form})