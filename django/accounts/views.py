from rest_framework import viewsets, permissions
from .models import CustomUser
from .serializers import CustomUserSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return CustomUser.objects.all()
        return CustomUser.objects.filter(restaurant=self.request.user.restaurant)
