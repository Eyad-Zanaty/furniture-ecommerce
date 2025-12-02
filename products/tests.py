from django.test import TestCase
from .models import Product, ProductImage, Cart
from users.models import CustomUser as User
# Create your tests here.

class ProductModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            product_category='Chairs',
            product_brand='Ikea',
            product_name='Test Chair',
            product_description='A comfortable test chair.',
            product_color='Red',
            product_price=100,
            product_instock=True
        )

    def test_product_creation(self):
        self.assertEqual(self.product.product_name, 'Test Chair')
        self.assertEqual(self.product.product_price, 100)
        self.assertTrue(self.product.product_instock)
        

class ProductImageModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            product_category='Chairs',
            product_brand='Ikea',
            product_name='Test Chair',
            product_description='A comfortable test chair.',
            product_color='Red',
            product_price=100,
            product_instock=True
        )
        self.product_image = ProductImage.objects.create(
            product_images=self.product
        )

    def test_product_image_creation(self):
        self.assertEqual(self.product_image.product_images, self.product)
        
class CartModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            product_category='Chairs',
            product_brand='Ikea',
            product_name='Test Chair',
            product_description='A comfortable test chair.',
            product_color='Red',
            product_price=100,
            product_instock=True
        )
        self.user = User.objects.create_user(first_name='testuser', last_name='user', email='testuser@example.com', password='12345')
        self.cart_item = Cart.objects.create(
            cart_user=self.user,
            cart_product=self.product,
            cart_quantity=2,
            cart_sub_price=self.product.product_price * 2,
            cart_delivery_fees=10,
            cart_total_price=self.product.product_price * 2 + 10
        )

    def test_cart_creation(self):
        self.assertEqual(self.cart_item.cart_user, self.user)
        self.assertEqual(self.cart_item.cart_product, self.product)
        self.assertEqual(self.cart_item.cart_quantity, 2)
        self.assertEqual(self.cart_item.cart_sub_price, self.product.product_price * 2)
        self.assertEqual(self.cart_item.cart_delivery_fees, 10)
        self.assertEqual(self.cart_item.cart_total_price, self.product.product_price * 2 + 10)