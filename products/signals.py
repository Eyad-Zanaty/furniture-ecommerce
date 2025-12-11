from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from products.models import Product
from users.models import CustomUser as User

@receiver([post_save, post_delete], sender=Product)
def clear_product_cache(sender, **kwargs):
    cache.delete_pattern('*shop_page*')
    
@receiver([post_save, post_delete], sender=User)
def clear_user_cache(sender, **kwargs):
    cache.delete_pattern('*shop_page*')