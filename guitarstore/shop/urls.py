# shop/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, OrderViewSet, GuitarViewSet, GuitarCategoryViewSet, ShoppingCartViewSet
from django.urls import path
from . import views
from django.urls import path
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, OrderViewSet, GuitarViewSet, GuitarCategoryViewSet, ShoppingCartViewSet, simple_order_create
from django.urls import path
from .views import order_create, order_success
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'guitars', GuitarViewSet)
router.register(r'categories', GuitarCategoryViewSet)
router.register(r'carts', ShoppingCartViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('simple_orders/', order_create, name='order_create'),
    path('order-success/', order_success, name='order_success'),
]

