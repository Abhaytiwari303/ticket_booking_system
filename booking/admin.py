from django.contrib import admin
from .models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('user', 'service_type', 'booking_date', 'slot_time', 'status')
    list_filter = ('booking_date', 'status')
    search_fields = ('user__username', 'service_type')
