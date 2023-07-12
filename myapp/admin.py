from django.contrib import admin

from .models import Appointment


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('appointment_date','appointment_time', 'full_name', 'your_email','your_phone','your_address','message')  # Customize the displayed fields

admin.site.register(Appointment, AppointmentAdmin)

# Register your models here.
