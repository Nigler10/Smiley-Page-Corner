from django.db import models
from products.models import Product

class CakeOption(models.Model):
    OPTION_TYPE_CHOICES = [
        ('size', 'Size'),
        ('flavor', 'Flavor'),
        ('icing', 'Icing'),
        ('topping', 'Topping'),
        ('color', 'Color'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="options")
    option_type = models.CharField(max_length=50, choices=OPTION_TYPE_CHOICES)
    name = models.CharField(max_length=100)
    additional_price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.product.name} - {self.name}"
