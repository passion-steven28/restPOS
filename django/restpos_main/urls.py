from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from accounts.views import CustomUserViewSet
from restaurants.views import RestaurantViewSet, TableViewSet
from products.views import ProductViewSet
from orders.views import OrderViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r"users", CustomUserViewSet)
router.register(r"restaurants", RestaurantViewSet)
router.register(r"tables", TableViewSet)
router.register(r"products", ProductViewSet)
router.register(r"orders", OrderViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
