from django.db import models
from products.models import Product
from django.utils import timezone

class CustomerPreference(models.Model):
    name = models.CharField(max_length=150)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="preferences"
    )
    favorite_flavor = models.CharField(max_length=100)
    preferred_size = models.CharField(max_length=50)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} → {self.product.name}"
