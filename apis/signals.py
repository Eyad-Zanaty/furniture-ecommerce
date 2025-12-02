from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from products.models import Product

@receiver([post_save, post_delete], sender=Product)
def invalid_product_cache(sender, **kwargs):
    cache.delete_pattern('*product_api_cache*')