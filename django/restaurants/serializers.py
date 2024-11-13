# restaurants/serializers.py
from rest_framework import serializers
from .models import Restaurant, Table


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ["id", "name", "address", "phone", "owner", "created_at", "is_active"]
        read_only_fields = ["owner"]


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = "__all__"
