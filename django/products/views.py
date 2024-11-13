from django.shortcuts import render
from rest_framework import viewsets
from django_filters import rest_framework as filters
from .models import Product
from .serializers import ProductSerializer


class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = filters.NumberFilter(field_name="price", lookup_expr="lte")

    class Meta:
        model = Product
        fields = ["restaurant", "category", "is_available", "min_price", "max_price"]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    search_fields = ["name", "description"]
    ordering_fields = ["name", "price"]
