from rest_framework import serializers
from .models import CustomerPreference

class CustomerPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerPreference
        fields = "__all__"
