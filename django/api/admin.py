from django.contrib import admin

from api.models import Product, Category,Order,OrderItem,Reservation,Table,UserProfile

# Register your models here.
admin.site.register([Product,Category, Order,OrderItem,Reservation,Table,UserProfile])

