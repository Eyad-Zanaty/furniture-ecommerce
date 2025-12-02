from django.urls import path, include
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('shop/<int:pk>/', views.product_details, name='product-details'),
    path('cart/', views.cart, name='cart'),
]
