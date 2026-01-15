from rest_framework import serializers
from .models import DeliveryTracking

class DeliveryTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryTracking
        fields = "__all__"
