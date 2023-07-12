from django.db import models

class Appointment(models.Model):
    appointment_date = models.DateTimeField(blank=True, null=True)
    appointment_time = models.TimeField()
    full_name = models.CharField(max_length=100)
    your_email = models.EmailField()
    your_phone = models.CharField(max_length=20, null=True)
    your_address = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.appointment_form_full_name
