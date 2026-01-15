from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('product', 'rating', 'customer_name', 'created_at')
    list_filter = ('rating',)
