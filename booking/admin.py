from django.contrib import admin
from .models import Booking
# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('expert', 'customer', 'checkin', 'checkout', 'location', 'created_at', 'updated_at')
    list_filter = ('checkin', 'checkout', 'created_at', 'updated_at')
    search_fields = ('expert__username', 'customer__username', 'location')