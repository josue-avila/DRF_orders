from django.urls import path, include
from rest_framework import routers
from DRF_orders.orders.views import ProductViewSet, OrderViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'orders', OrderViewSet, basename='orders')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include(
        'rest_framework.urls', namespace='rest_framework'))
]
