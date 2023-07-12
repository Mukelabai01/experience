from django import forms
from django.forms import ModelForm
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['appointment_date', 'appointment_time', 'full_name', 'your_email','your_phone','your_address','message']
        widgets ={
            'appointment_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Select Date', 'type': 'date'}),
            'appointment_time': forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'Select Time', 'type': 'time'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'your_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),         
            'your_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Number'}),
            'your_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'your_address'}),
            'message': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
                }

        

