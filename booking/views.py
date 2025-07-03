from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm, TicketForm
from .models import Ticket, Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import Ticket


def booked_slots(request):
    events = []
    for ticket in Ticket.objects.all():
        events.append({
            'title': ticket.service_type,
            'start': f"{ticket.booking_date}T{ticket.slot_time}",
            'end': f"{ticket.booking_date}T{ticket.slot_time}",  # You can add +duration if needed
        })
    return JsonResponse(events, safe=False)



def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(
                user=user,
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                address=form.cleaned_data['address'],
                phone=form.cleaned_data['phone'],
                photo=form.cleaned_data['photo']
            )
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'booking/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'booking/login.html', {'form': form})

@login_required
def dashboard(request):
    form = TicketForm()
    bookings = Ticket.objects.filter(user=request.user)  # ← this is key
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user  # ← link ticket to user
            ticket.save()
            return redirect('dashboard')
    return render(request, 'booking/dashboard.html', {'form': form, 'bookings': bookings})



def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def admin_dashboard(request):
    if not request.user.is_superuser:
        return redirect('dashboard')
    users = Profile.objects.all()
    tickets = Ticket.objects.all()
    return render(request, 'booking/admin_dashboard.html', {'users': users, 'tickets': tickets})
