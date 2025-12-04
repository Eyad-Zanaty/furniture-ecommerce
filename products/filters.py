from django import forms
import django_filters
from .models import Product

category_choices= [
        ('Chairs', 'Chairs'),
        ('Beds', 'Beds'),
        ('Accessories', 'Accessories'),
        ('Furniture', 'Furniture'),
        ('Home Deco', 'Home Deco'),
        ('Dressings', 'Dressings'),
        ('Tables', 'Tables'),
    ]

brand_choices= [
        ('Ikea', 'Ikea'),
        ('Amado', 'Amado'),
        ('Furniture Inc', 'Furniture Inc'),
        ('The factory', 'The factory'),
        ('Artdeco', 'Artdeco'),
]



class ProductFilter(django_filters.FilterSet):
    product_category= django_filters.ChoiceFilter(field_name= 'product_category', choices=category_choices)
    product_brand= django_filters.MultipleChoiceFilter(field_name= 'product_brand', choices=brand_choices, widget=forms.CheckboxSelectMultiple)
    product_name= django_filters.CharFilter(field_name='product_name', lookup_expr='icontains')
    product_color= django_filters.CharFilter(field_name= 'product_color', lookup_expr='iexact')
    min_price = django_filters.NumberFilter(field_name='product_price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='product_price', lookup_expr='lte')
    
    class Meta:
        model= Product
        fields={
            'product_category': ['exact'],
            'product_brand': ['contains'],
            'product_name': ['icontains'],
            'product_color': ['exact'],
            'product_price': ['exact'],
        }