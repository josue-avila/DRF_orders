from django.contrib import admin
from .models import Product, Order


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
admin.site.register(Product, ProductAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'order_code', 'id_channel',
        'id_seller', 'date'
    )
admin.site.register(Order, OrderAdmin) 
