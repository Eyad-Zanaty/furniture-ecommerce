from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from products.models import Cart, Subscribtions
from .forms import CheckoutForm
from users.models import CustomUser as User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

@login_required
@csrf_exempt
def checkout_view(request):
    cart_items = Cart.objects.filter(cart_user=request.user)

    # Calculate subtotal and total price
    sub_price = 0
    total_price = 0
    for item in cart_items:
        sub_price+= item.cart_sub_price
        total_price+= item.cart_total_price
        
    # Handle form submission
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['checkout_create_account'] == True:
                User.objects.get_or_create(
                    first_name=form.cleaned_data['checkout_firstname'],
                    last_name=form.cleaned_data['checkout_lastname'],
                    email=form.cleaned_data['checkout_email'],
                    phone_number=form.cleaned_data['checkout_phone_number'],
                    address=form.cleaned_data['checkout_address'],
                    payment_method='Cash',
                    password='defaultpassword'
                )
                
            form.save()
    else:
        form = CheckoutForm()
    
    if request.method == 'POST' and 'logout' in request.POST:
        logout(request)
        return redirect('users:login')
    
    
    if request.method == 'POST' and 'email_subscription' in request.POST:
        email= request.POST.get('email_subscription')
        Subscribtions.objects.create(
            subscribtion_user= request.user,
            subscribtions_email= email,
        )
        
        message=f"""Hi {request.user.first_name},

Subscription confirmed — welcome to the community!
        """
        send_mail(
            "Furniture Payment",
            message,
            settings.EMAIL_HOST_USER,
            [request.user.email],
            fail_silently=False,
        )
    
    context={
        'sub_price': sub_price,
        'total_price': total_price,
        'cart_items': cart_items,
        'form': CheckoutForm,
    }
    return render(request, 'payment/checkout.html', context)
