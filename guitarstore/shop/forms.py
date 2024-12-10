from django import forms
from .models import Order
from .models import SimpleOrder

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user', 'total_price', 'order_status'] 

class SimpleOrderForm(forms.ModelForm):
    class Meta:
        model = SimpleOrder
        fields = ['items', 'total_price']