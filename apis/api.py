from products.models import Product, Cart
from payment.models import checkout, order
from users.models import CustomUser as User
from apis.serializers import ProductSerializer, UserSerializer, CartSerializer, CheckoutSerializer, OrderSerializer
from rest_framework import generics
from rest_framework import permissions
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

@method_decorator(cache_page(60 * 15, key_prefix='product_api_cache'), name='dispatch')
class ProductView(
    generics.ListAPIView,
    generics.CreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    


class UserView(
    generics.ListAPIView,
    generics.CreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView, generics.RetrieveAPIView
):
    queryset= User.objects.all()
    serializer_class= UserSerializer
    permission_classes= [permissions.IsAdminUser]
    
        

class CartView(
    generics.ListAPIView,
    generics.CreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView, generics.RetrieveAPIView
):
    queryset= Cart.objects.all()
    serializer_class= CartSerializer
    permission_classes= [permissions.IsAuthenticated]
    

class CheckoutView(
    generics.ListAPIView,
    generics.CreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView, generics.RetrieveAPIView
):
    queryset= checkout.objects.all()
    serializer_class= CheckoutSerializer
    permission_classes= [permissions.IsAuthenticated]

class OrderView(
    generics.ListAPIView,
    generics.CreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView, generics.RetrieveAPIView
):
    queryset= order.objects.all()
    serializer_class= OrderSerializer
    permission_classes= [permissions.IsAuthenticatedOrReadOnly]