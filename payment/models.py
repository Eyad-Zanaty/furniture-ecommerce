from django.db import models
from users.models import CustomUser

# Create your models here.

checkout_country_choices = [
    ('USA', 'United States'),
    ('MEX', 'Mexico'),
    ('EGY', 'Egypt'),
    ('CAN', 'Canada'),
    ('UK', 'United Kingdom'),
    ('AUS', 'Australia'),
    ('IND', 'India'),
    ('GER', 'Germany'),
    ('FRA', 'France'),
    ('JPN', 'Japan'),
    ('CHN', 'China'),
    ('BRA', 'Brazil'),
]


class checkout(models.Model):
    checkout_firstname = models.CharField(max_length=30)
    checkout_lastname = models.CharField(max_length=3)
    checkout_company_name = models.CharField(max_length=100, blank=True, null=True)
    checkout_email = models.EmailField()
    checkout_country = models.CharField(max_length=50, choices=checkout_country_choices)
    checkout_town = models.CharField(max_length=255)
    checkout_address = models.CharField(max_length=255)
    checkout_zipcode = models.CharField(max_length=20)
    checkout_phone_number = models.CharField(max_length=20)
    checkout_order_comment = models.TextField(blank=True, null=True)
    checkout_create_account = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Checkout of {self.checkout_firstname} {self.checkout_lastname} at {self.created_at}"
    
class order(models.Model):
    order_checkout = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    order_total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.CharField(max_length=50, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.order_status}"