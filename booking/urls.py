from django.urls import path
from . import views
from django.shortcuts import redirect


urlpatterns = [
    path('', lambda r: redirect('login')),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('api/booked-slots/', views.booked_slots, name='booked-slots'),
]
