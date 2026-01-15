from rest_framework import serializers
from .models import CakeOption

class CakeOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CakeOption
        fields = "__all__"
