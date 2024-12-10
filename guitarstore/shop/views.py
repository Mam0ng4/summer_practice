from rest_framework import viewsets
from .models import User, Order, Guitar, GuitarCategory, ShoppingCart, OrderGuitar
from .serializers import UserSerializer, OrderSerializer, GuitarSerializer, GuitarCategorySerializer, ShoppingCartSerializer
from django.shortcuts import render
import logging
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import SimpleOrder, Guitar
logger = logging.getLogger(__name__)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class GuitarViewSet(viewsets.ModelViewSet):
    queryset = Guitar.objects.all()
    serializer_class = GuitarSerializer

class GuitarCategoryViewSet(viewsets.ModelViewSet):
    queryset = GuitarCategory.objects.all()
    serializer_class = GuitarCategorySerializer

class ShoppingCartViewSet(viewsets.ModelViewSet):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer

@api_view(['POST'])

def simple_order_create(request):
    data = request.data
    try:
        order_data = {
            'first_name': data['first_name'],
            'last_name': data['last_name'],
            'email': data['email'],
            'total_price': data['total_price'],
            'order_status': 'pending',
            'items': data['items']
        }
        order_serializer = SimpleOrderSerializer(data=order_data)

        if order_serializer.is_valid():
            order_serializer.save()
            return Response(order_serializer.data, status=status.HTTP_201_CREATED)
        else:
            logger.error(f"Simple Order serializer errors: {order_serializer.errors}")
            return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        logger.error(f"Error creating simple order: {e}")
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

def order_create(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        order = SimpleOrder(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            total_price=data['total_price'],
        )
        order.save()
        for item in data['items']:
            guitar = Guitar.objects.get(id=item['guitar_id'])
            order.guitars.add(guitar)
        return JsonResponse({'message': 'Order created successfully'})
    return JsonResponse({'error': 'Invalid request method'}, status=400)

def order_success(request):
    return render(request, 'shop/order_success.html')