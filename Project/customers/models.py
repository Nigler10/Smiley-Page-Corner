from django.db import models

class CustomerPreference(models.Model):
    name = models.CharField(max_length=150)
    favorite_flavor = models.CharField(max_length=100)
    preferred_size = models.CharField(max_length=50)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name
