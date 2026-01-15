from django.contrib import admin
from .models import CustomerPreference

@admin.register(CustomerPreference)
class CustomerPreferenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'favorite_flavor', 'preferred_size')
