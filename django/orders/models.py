from django.db import models
from accounts.models import CustomUser
from restaurants.models import Restaurant
from products.models import Product


class Order(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("preparing", "Preparing"),
        ("ready", "Ready"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    ]

    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="orders"
    )
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="orders"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
