from django.urls import path, include
from . import api

app_name = 'api'
urlpatterns = [
    path('products/', api.ProductView.as_view(), name='product-list'),
    path('users/', api.UserView.as_view(), name='users-list'),
    path('carts/', api.CartView.as_view(), name='carts-list'),
    path('checkouts/', api.CheckoutView.as_view(), name='checkouts-list'),
    path('orders/', api.OrderView.as_view(), name='orders-list'),
]