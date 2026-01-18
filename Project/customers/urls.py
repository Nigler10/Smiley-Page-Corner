from django.urls import path
from . import views

urlpatterns = [
    path("products/<int:product_id>/preference/", views.create_preference, name="preference-create"),
    path("preferences/success/", views.preference_success, name="preference-success"),
]
