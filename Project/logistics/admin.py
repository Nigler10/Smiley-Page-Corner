from django.contrib import admin
from .models import DeliveryTracking

@admin.register(DeliveryTracking)
class DeliveryTrackingAdmin(admin.ModelAdmin):
    list_display = ('tracking_number', 'courier', 'current_location', 'last_updated')
