from django.test import TestCase
from django.urls import reverse
from .models import checkout, order
from users.models import CustomUser as User
# Create your tests here.

class CheckoutModelTest(TestCase):
    def setUp(self):
        self.checkout = checkout.objects.create(
            checkout_firstname="John",
            checkout_lastname="Doe",
            checkout_email="john.doe@example.com",
            checkout_country="USA",
            checkout_town="New York",
            checkout_address="123 Main St",
            checkout_zipcode="10001",
            checkout_phone_number="1234567890"
        )
        
    def test_checkout_creation(self):
        self.assertEqual(self.checkout.checkout_firstname, "John")
        self.assertEqual(self.checkout.checkout_lastname, "Doe")
        self.assertEqual(self.checkout.checkout_email, "john.doe@example.com")
        self.assertEqual(self.checkout.checkout_country, "USA")
        self.assertEqual(self.checkout.checkout_town, "New York")
        self.assertEqual(self.checkout.checkout_address, "123 Main St")
        self.assertEqual(self.checkout.checkout_zipcode, "10001")
        self.assertEqual(self.checkout.checkout_phone_number, "1234567890")
        

class OrderModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            first_name='testuser', 
            last_name='user', 
            email='testuser@example.com', 
            password='12345')
        
    def test_user_creation(self):
        user= User.objects.get(email=self.user.email)
        self.client.login(email=self.user.email, password=self.user.password)
        
        def test_paymob(self):
            response = self.client.post(reverse('payment:paymob'))
            self.assertEqual(response.status_code, 302)
            
    def test_order_creation(self):
        order_instance = order.objects.create(
            order_checkout=self.user,
            order_total_price=99.99
        )
        self.assertEqual(order_instance.order_checkout, self.user)
        self.assertEqual(order_instance.order_total_price, 99.99)
        self.assertEqual(order_instance.order_status, 'Pending')