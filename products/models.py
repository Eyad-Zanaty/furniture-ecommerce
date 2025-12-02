from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms import ValidationError
from django.conf import settings
from users.models import CustomUser

# Create your models here.


prod_brand= [
    ('Ikea', 'Ikea'),
    ('Amado', 'Amado'),
    ('Furniture Inc', 'Furniture Inc'),
    ('The factory', 'The factory'),
    ('Artdeco', 'Artdeco'),
]


prod_cat=[
    ('Chairs', 'Chairs'),
    ('Beds', 'Beds'),
    ('Accessories', 'Accessories'),
    ('Furnitures', 'Furnitures'),
    ('Home Deco', 'Home Deco'),
    ('Dressings', 'Dressings'),
    ('Tables', 'Tables'),
]

prod_col=[
    ('Red', 'Red'),
    ('Blue', 'Blue'),
    ('Green', 'Green'),
    ('Yellow', 'Yellow'),
    ('Black', 'Black'),
    ('White', 'White'),
    ('Brown', 'Brown'),
    ('Grey', 'Grey'),
]

class Product(models.Model):
    product_category= models.CharField(max_length=100, choices=prod_cat)
    product_brand=models.CharField(max_length=100, choices=prod_brand)
    product_name=models.CharField(max_length=100)
    product_description=models.TextField(max_length=500)
    product_color= models.CharField(max_length=100, choices=prod_col)
    product_price= models.IntegerField(validators=[
            MinValueValidator(1),
            MaxValueValidator(10000000),
        ])
    product_instock=models.BooleanField(default=True)
    product_date=models.DateTimeField(auto_now_add=True)
    product_image= models.ImageField(upload_to='products_image/%y/%m/%d/', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Products'
        ordering = ['-product_date']
    
    def __str__(self):
        return self.product_name
    

class ProductImage(models.Model):
    product_images= models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        related_name='product_images',
    )
    product_uploaded_image=models.ImageField(upload_to='products_image/%y/%m/%d/images')
    product_image_date=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Product Images'
        ordering = ['-product_image_date']
    
    def image_limiter(self):
        existing_images = ProductImage.objects.filter(product_images=self.product_images).count()
        if existing_images > 4:
            raise ValidationError("You can upload a maximum of 4 images per product.")
    
    def __str__(self):
        self.image_limiter()
        return self.product_image_date.strftime("%Y-%m-%d %H:%M:%S")

    
class Cart(models.Model):
        cart_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart_user')
        cart_product = models.ForeignKey(Product, on_delete=models.CASCADE)
        cart_quantity = models.PositiveIntegerField(default=1)
        cart_sub_price = models.DecimalField(max_digits=10, decimal_places=2)
        cart_delivery_fees = models.DecimalField(max_digits=10, decimal_places=2)
        cart_total_price = models.DecimalField(max_digits=10, decimal_places=2)

        class Meta:
            verbose_name = 'Cart'
            ordering = ['cart_user']
            
        
        def __str__(self):
            return f"{self.cart_quantity} of {self.cart_product.product_name} for {self.cart_user.first_name} {self.cart_user.last_name}"

class Subscribtions(models.Model):
    subscribtion_user= models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    subscribtions_email= models.EmailField()
    subscribtion_date= models.DateTimeField(auto_now_add=True)