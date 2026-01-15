from django.db import models
from orders.models import Order

class DeliveryTracking(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name="tracking")
    tracking_number = models.CharField(max_length=100, unique=True)
    courier = models.CharField(max_length=100)
    last_updated = models.DateTimeField(auto_now=True)
    current_location = models.CharField(max_length=255)

    def __str__(self):
        return self.tracking_number
