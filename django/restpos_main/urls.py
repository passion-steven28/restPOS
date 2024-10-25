from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from api.views import ProductList, CategoryList, OrderList, OrderItemList, ReservationList, UserProfileList

router = DefaultRouter()
router.register(r'products', ProductList)
router.register(r'categories', CategoryList)
router.register(r'orders', OrderList)
router.register(r'orderitems', OrderItemList)
router.register(r'reservations', ReservationList)
router.register(r'userprofiles', UserProfileList)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
