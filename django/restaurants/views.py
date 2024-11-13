from django.shortcuts import render

# restaurants/views.py
from rest_framework import viewsets, permissions
from .models import Restaurant, Table
from .serializers import RestaurantSerializer, TableSerializer
from .permissions import IsOwnerOrAdmin


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Restaurant.objects.all()
        return Restaurant.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Table.objects.all()
        return Table.objects.filter(restaurant__owner=self.request.user)
