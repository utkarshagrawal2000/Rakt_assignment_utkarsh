from rest_framework import serializers
from .models import FoodTruck

class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()


class FoodTruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodTruck
        fields = "__all__"