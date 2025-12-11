from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.db.models import Min
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from .models import Product, ProductImage, Cart, Subscribtions
from .filters import ProductFilter
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
@csrf_exempt
@login_required
def home(request):
    cart_items= Cart.objects.filter(cart_user= request.user)
    # getting each item least price
    def least_price(product='none'):
        leastprice = Product.objects.filter(product_instock=True, product_category=product).aggregate(Min('product_price'))
        return leastprice
    
    if request.method == 'POST' and 'logout' in request.POST:
        logout(request)
        return redirect('users:login')
    
    
    # Isn't allowed on Railway
    
#     if request.method == 'POST' and 'email_subscription' in request.POST:
#         email= request.POST.get('email_subscription')
#         Subscribtions.objects.create(
#             subscribtion_user= request.user,
#             subscribtions_email= email,
#         )
        
#         message=f"""Hi {request.user.first_name},

# Subscription confirmed — welcome to the community!
#         """
#         send_mail(
#             "Furniture Payment",
#             message,
#             settings.EMAIL_HOST_USER,
#             [request.user.email],
#             fail_silently=False,
#         )
    
    context={
        'chairs': least_price('Chairs'),
        'home_deco': least_price('Home Deco'),
        'tables': least_price('Tables'),
        'cart_items': cart_items,
    }
    return render(request, 'products/home.html', context)

@login_required
@csrf_exempt
@cache_page(60 * 15, key_prefix='shop_page') 
def shop(request):
    # Queryset of products
    products= Product.objects.filter()
    
    cart_items= Cart.objects.filter(cart_user= request.user)
    
    if 'select_order' in request.GET:
        per_page = request.GET.get('select_order')
        if per_page == 'date':
            products= products.order_by('product_date')
        elif per_page == 'newest':
            products= products.order_by('-product_date')
        elif per_page == 'popular':
            products= products.order_by('-product_price')
            
    if 'add_to_cart_btn' in request.POST:
        product_id = request.POST.get('add_to_cart_btn')
        product = Product.objects.get(id=product_id)
        cart_item, created = Cart.objects.get_or_create(
        cart_user=request.user,
        cart_product=product,
        defaults={
            "cart_quantity": 1,
            "cart_sub_price": product.product_price,
            "cart_delivery_fees": 50,
            "cart_total_price": product.product_price + 50,
        },
        )
        cart_item.save()
        
        if not created:
                cart_item.cart_quantity += 1
                cart_item.cart_sub_price = product.product_price * cart_item.cart_quantity
                cart_item.cart_total_price = cart_item.cart_sub_price + cart_item.cart_delivery_fees
                cart_item.save()

                return redirect('products:cart')
        
    
    if request.method == 'POST' and 'logout' in request.POST:
        logout(request)
        return redirect('users:login')
    
    # Isn't allowed on Railway
    
#     if request.method == 'POST' and 'email_subscription' in request.POST:
#         email= request.POST.get('email_subscription')
#         Subscribtions.objects.create(
#             subscribtion_user= request.user,
#             subscribtions_email= email,
#         )
        
#         message=f"""Hi {request.user.first_name},

# Subscription confirmed — welcome to the community!
#         """
#         send_mail(
#             "Furniture Payment",
#             message,
#             settings.EMAIL_HOST_USER,
#             [request.user.email],
#             fail_silently=False,
#         )
    
    # Apply filters
    myfilter= ProductFilter(request.GET, queryset=products)
    products= myfilter.qs
    
    # Pagination
    products_per_page = request.GET.get('select_product_number')
    per_page = int(products_per_page) if products_per_page else 8
    paginator = Paginator(products, per_page)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    
    context={
        'products': page_obj,
        'myfilter': myfilter,
        'cart_items': cart_items,
    }
    return render(request, 'products/shop.html', context)

@login_required
@csrf_exempt
def product_details(request, pk):
    # Get the product by its primary key
    product= Product.objects.get(id=pk)
    product_images= ProductImage.objects.filter(product_images=product)
    
    cart_items= Cart.objects.filter(cart_user= request.user)
    
    # Add to cart functionality
    if request.method == 'POST':
        add_to_cart = request.POST.get('addtocart')
        if add_to_cart:
            quantity = int(request.POST.get('quantity', 1))
            cart_item, created = Cart.objects.get_or_create(
                cart_user=request.user,
                cart_product=product,
                defaults={
                    "cart_quantity": quantity,
                    "cart_sub_price": product.product_price * quantity,
                    "cart_delivery_fees": 50,
                    "cart_total_price": (product.product_price * quantity) + 50,
                }
            )
            
            if not created:
                cart_item.cart_quantity = quantity
                cart_item.cart_sub_price = product.product_price * cart_item.cart_quantity
                cart_item.cart_total_price = cart_item.cart_sub_price + cart_item.cart_delivery_fees
                cart_item.save()

            cart_item.save()
            
            
    if request.method == 'POST' and 'logout' in request.POST:
        logout(request)
        return redirect('users:login')
    
    
    # Isn't allowed on Railway
    
#     if request.method == 'POST' and 'email_subscription' in request.POST:
#         email= request.POST.get('email_subscription')
#         Subscribtions.objects.create(
#             subscribtion_user= request.user,
#             subscribtions_email= email,
#         )
        
#         message=f"""Hi {request.user.first_name},

# Subscription confirmed — welcome to the community!
#         """
#         send_mail(
#             "Furniture Payment",
#             message,
#             settings.EMAIL_HOST_USER,
#             [request.user.email],
#             fail_silently=False,
#         )
    
    
    context={
        'product': product,
        'product_images': product_images,
        'cart_items': cart_items,
    }
    return render(request, 'products/product-details.html', context)


@login_required
@csrf_exempt
def cart(request):
    # Get cart items for the logged-in user
    cart_items= Cart.objects.filter(cart_user= request.user)
    
    # Calculate subtotal and total prices
    sub_prices = 0
    total_prices = 0
    for item in cart_items:
        sub_prices+= item.cart_sub_price
        total_prices+= item.cart_total_price
    
    if request.method == "POST":
        
        item_id = request.POST.get("item_id")

        if item_id:
                item = Cart.objects.get(id=item_id, cart_user=request.user)

                if item:
                    quantity = int(request.POST.get("cart_quantity", 1))

                    if quantity < 1:
                        quantity = 1

                    item.cart_quantity = quantity
                    item.cart_sub_price = item.cart_product.product_price * quantity
                    item.cart_total_price = item.cart_sub_price + item.cart_delivery_fees
                    item.save()
        
    
    if request.method == 'POST' and 'logout' in request.POST:
        logout(request)
        return redirect('users:login')
    
    
    # Isn't allowed on Railway
    
#     if request.method == 'POST' and 'email_subscription' in request.POST:
#         email= request.POST.get('email_subscription')
#         Subscribtions.objects.create(
#             subscribtion_user= request.user,
#             subscribtions_email= email,
#         )
        
#         message=f"""Hi {request.user.first_name},

# Subscription confirmed — welcome to the community!
#         """
#         send_mail(
#             "Furniture Payment",
#             message,
#             settings.EMAIL_HOST_USER,
#             [request.user.email],
#             fail_silently=False,
#         )
    
    context={
        'cart_items': cart_items,
        'sub_prices': sub_prices,
        'total_prices': total_prices,
    }
    return render(request, 'products/cart.html', context)