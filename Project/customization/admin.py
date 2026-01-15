from django.contrib import admin
from .models import CakeOption

@admin.register(CakeOption)
class CakeOptionAdmin(admin.ModelAdmin):
    list_display = ('product', 'option_type', 'name', 'additional_price')
    list_filter = ('option_type',)
