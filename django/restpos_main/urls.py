from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from api.views import ProductList, CategoryList, OrderList, OrderItemList, ReservationList, UserProfileList
from rest_framework.authtoken import views
from auth_app.views import UserApiView

router = DefaultRouter()
router.register(r'products', ProductList)
router.register(r'categories', CategoryList)
router.register(r'orders', OrderList)
router.register(r'orderitems', OrderItemList)
router.register(r'reservations', ReservationList)
router.register(r'user', UserApiView)
# router.register(r'analytics', AnalyticsInfoView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token)
]
