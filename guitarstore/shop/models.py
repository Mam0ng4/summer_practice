# shop/models.py
from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
class GuitarCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)

class Guitar(models.Model):
    guitar_id = models.AutoField(primary_key=True)
    guitar_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    manufacturer = models.CharField(max_length=100)
    country_of_origin = models.CharField(max_length=100)
    year_of_production = models.IntegerField()
    image_url = models.URLField()
    category = models.ForeignKey(GuitarCategory, on_delete=models.CASCADE)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.CharField(max_length=20, default='pending')

    def __str__(self):
        return f"Order {self.pk} by {self.user.email}"

class OrderGuitar(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    guitar = models.ForeignKey(Guitar, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

class ShoppingCart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    guitars_count = models.PositiveIntegerField()
    guitar = models.ForeignKey(Guitar, on_delete=models.CASCADE)

class SimpleOrder(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.CharField(max_length=20, default='pending')

    def __str__(self):
        return f"Order {self.pk} - {self.email}"

class SimpleOrderGuitar(models.Model):
    order = models.ForeignKey(SimpleOrder, on_delete=models.CASCADE)
    guitar = models.ForeignKey(Guitar, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()