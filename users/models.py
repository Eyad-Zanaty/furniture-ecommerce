from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None, is_staff=False, is_superuser=False, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        elif not first_name:
            raise ValueError('The First Name field must be set')
        elif not last_name:
            raise ValueError('The Last Name field must be set')
        
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()
        return user

    def create_superuser(self, email, first_name, last_name, password=None, **extra_fields):
        user= self.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            is_staff=True,
            is_superuser=True,
            **extra_fields)

        user.save()
        return user



class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    payment_method = models.CharField(max_length=50, blank=True, null=True)
    
    username = None  # Remove username field
    USERNAME_FIELD = 'email'  # Use email as the unique identifier
    REQUIRED_FIELDS = ['first_name', 'last_name']
    objects = UserManager()