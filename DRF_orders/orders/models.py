from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    price = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return f"Product - {self.name}"


class Order(models.Model):
    order_code = models.CharField(max_length=100, null=False, blank=False)
    id_channel = models.IntegerField(null=True, blank=True)
    id_seller = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f"Order - {self.order_code}"
