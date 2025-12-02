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
    product_category= django_filters.ChoiceFilter(choices=category_choices)
    product_brand= django_filters.MultipleChoiceFilter(choices=brand_choices, widget=forms.CheckboxSelectMultiple)
    product_color= django_filters.CharFilter(lookup_expr='iexact')
    min_price = django_filters.NumberFilter(field_name='product_price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='product_price', lookup_expr='lte')
    
    class Meta:
        model= Product
        fields={
            'product_category': ['exact'],
            'product_brand': ['contains'],
            'product_name': ['contains'],
            'product_color': ['exact'],
            'product_price': ['exact'],
        }