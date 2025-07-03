from django.db import models
from django.contrib.auth.models import User
from datetime import date  # for default


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='profile_photos/')

    def __str__(self):
        return self.user.username

class Ticket(models.Model):
    SERVICE_CHOICES = [
        ('General Service', 'General Service'),
        ('Premium Service', 'Premium Service'),
        ('Consultation', 'Consultation'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=100, choices=SERVICE_CHOICES)
    booking_date = models.DateField()
    slot_time = models.TimeField()
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"{self.service_type} - {self.booking_date} {self.slot_time}"

