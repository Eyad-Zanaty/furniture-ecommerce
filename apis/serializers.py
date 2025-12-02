from rest_framework import serializers
from products.models import Product, ProductImage, Cart
from payment.models import checkout, order
from users.models import CustomUser as User


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    product_images = ProductImageSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ['product_category', 'product_brand', 'product_name', 'product_description', 'product_color', 'product_price', 'product_instock', 'product_date', 'product_image', 'product_images']

class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = checkout
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']

class ViewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']
        
class OrderSerializer(serializers.ModelSerializer):
    order_checkout = ViewUserSerializer(read_only=True)
    class Meta:
        model = order
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    cart_user= ViewUserSerializer(read_only=True)
    class Meta:
        model= Cart
        fields= '__all__'