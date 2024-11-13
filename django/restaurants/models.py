from django.db import models
from django.conf import settings


class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    # Use string reference for owner
    owner = models.ForeignKey(
        "accounts.CustomUser",
        on_delete=models.PROTECT,
        related_name="owned_restaurants",
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Table(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="tables"
    )
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    is_available = models.BooleanField(default=True)
