from django.contrib.auth.models import User
from rest_framework import permissions
from .serializers import UserSerializer
from rest_framework import viewsets

class UserApiView(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer
