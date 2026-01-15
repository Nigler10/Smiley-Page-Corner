from django.db import models
from products.models import Product

class Feedback(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="feedbacks")
    customer_name = models.CharField(max_length=150)
    rating = models.PositiveIntegerField()  # 1–5
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.rating}⭐"
