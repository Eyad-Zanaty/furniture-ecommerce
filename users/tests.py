from django.test import TestCase
from .models import CustomUser as User
# Create your tests here.

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            first_name='testuser',
            last_name='user',
            email='testuser@example.com',
            password='12345'
        )
    
    def test_user_creation(self):
        self.assertEqual(self.user.first_name, 'testuser')
        self.assertEqual(self.user.last_name, 'user')
        self.assertEqual(self.user.email, 'testuser@example.com')
        
    def test_user_permissions(self):
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)