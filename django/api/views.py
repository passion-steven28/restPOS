from django.shortcuts import render, get_list_or_404
from .models import Product, Category, Order, OrderItem, Reservation, UserProfile
from rest_framework.response import Response
from rest_framework.views import APIView
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
    
# class AnalyticsInfoView(APIView):
    def get(self, request):
        # get the total number of orders
        total_orders = Order.objects.all().count()
        # get the total number of products
        total_products = Product.objects.all().count()
        # get the total number of categories
        total_categories = Category.objects.all().count()
        # get the total number of reservations
        total_reservations = Reservation.objects.all().count()
        # get the total number of users
        total_users = UserProfile.objects.all().count()
        # get the total number of items ordered
        total_items_ordered = OrderItem.objects.all().count()
        # get the mouth revenue
        # total_revenue = Order.objects.all().aggregate(Sum('total_price'))['total_price__sum']
        
        return Response({
            'total_orders': total_orders,
            'total_products': total_products,
            'total_categories': total_categories,
            'total_reservations': total_reservations,
            'total_users': total_users
        })