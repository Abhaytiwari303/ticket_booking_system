from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Ticket

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    address = forms.CharField(widget=forms.Textarea)
    phone = forms.CharField()
    photo = forms.ImageField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['service_type', 'booking_date', 'slot_time']
        widgets = {
            'service_type': forms.Select(attrs={'class': 'form-select'}),
            'booking_date': forms.DateInput(attrs={
                'type': 'date', 'class': 'form-control'
            }),
            'slot_time': forms.TimeInput(attrs={
                'type': 'time', 'class': 'form-control'
            }),
        }