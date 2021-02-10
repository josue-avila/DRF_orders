from rest_framework import viewsets
from DRF_orders.orders.serializers import ProductSerializer, OrderSerializer
from DRF_orders.orders.models import Product, Order


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('order_code')
    serializer_class = OrderSerializer
