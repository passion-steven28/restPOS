from rest_framework import serializers
from .models import Order, OrderItem
from products.serializers import ProductSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    product_detail = ProductSerializer(source='product', read_only=True)
    
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_detail', 'quantity', 'price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    
    class Meta:
        model = Order
        fields = ['id', 'restaurant', 'user', 'created_at', 'total', 'status', 'items']
        read_only_fields = ['created_at']
    
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        
        return order

    def update(self, instance, validated_data):
        items_data = validated_data.pop('items', None)
        
        # Update Order fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        if items_data is not None:
            # Delete existing items
            instance.items.all().delete()
            
            # Create new items
            for item_data in items_data:
                OrderItem.objects.create(order=instance, **item_data)
        
        return instance
