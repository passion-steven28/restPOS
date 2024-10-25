from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Product, Category, Order, OrderItem, Reservation, UserProfile
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .serializers import ProductSerializer, CategorySerializer, OrderSerializer, OrderItemSerializer, ReservationSerializer, UserProfileSerializer

# Create your views here.
class ProductList(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryList(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class OrderList(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemList(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class ReservationList(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class UserProfileList(viewsets.ModelViewSet):
    # include the UserProfileSerializer in the response
    queryset = UserProfile.objects.all() 
    serializer_class = UserProfileSerializer