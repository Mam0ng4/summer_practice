# shop/serializers.py

from rest_framework import serializers
from .models import User, Order, Guitar, GuitarCategory, OrderGuitar, ShoppingCart
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'first_name', 'last_name', 'email', 'role')

class GuitarCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GuitarCategory
        fields = ('category_id', 'category_name')

class GuitarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guitar
        fields = '__all__'

class OrderGuitarSerializer(serializers.ModelSerializer):
    guitar_id = serializers.PrimaryKeyRelatedField(queryset=Guitar.objects.all(), source='guitar')

    class Meta:
        model = OrderGuitar
        fields = ['guitar_id', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    items = OrderGuitarSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'total_price', 'order_status', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            OrderGuitar.objects.create(order=order, **item_data)
        return order

class ShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = ['cart_id', 'guitars_count', 'guitar', 'user']