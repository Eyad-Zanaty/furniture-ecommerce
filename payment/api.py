import time
from rest_framework.decorators import api_view
from products.models import Cart
from .models import order
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import payment.paymob as paymob
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

@login_required
@api_view(['POST'])
def create_payment(request):
    cart_items = Cart.objects.filter(cart_user=request.user)

    # Calculate total price
    total_price = 0
    for item in cart_items:
        total_price += item.cart_total_price
        
    total_price_cents = int(total_price * 100)
    
    order_instance = order.objects.create(
        order_checkout=request.user,
        order_total_price=total_price,
    )

    # Paymob integration
    auth_token = paymob.Paymob.get_auth_token()
    order_response = paymob.Paymob.create_order(
        auth_token,
        total_price_cents,
        merchant_order_id=f"{order_instance.id}-{int(time.time())}"
    )  # amount in cents
    
    print("ORDER RESPONSE: ", order_response)
    paymob_order_id = order_response["id"]
    order_instance.paymob_order_id = paymob_order_id
    order_instance.save()

    payment_token = paymob.Paymob.get_payment_token(
        auth_token,
        paymob_order_id,
        total_price_cents,
        user=request.user
    )

    payment_url = f"{settings.PAYMOB_IFRAME_BASE_URL}?payment_token={payment_token}"

    return redirect(payment_url)


@csrf_exempt
@api_view(['POST', 'GET'])
def payment_callback(request):
    print("Callback hit!")
    print("Request method:", request.method)
    print("GET data:", request.GET)
    print("POST data:", request.data)
    
    data = request.GET

    
    merchant_order_id = data.get("merchant_order_id")
    print("merchant_order_id:", merchant_order_id)


    try:
        order_id_part = merchant_order_id.split("-")[0]
        order_id = int(order_id_part)
        print("order id:", order_id)
        get_order = order.objects.get(id=order_id)
    except Exception:
        return Response({"detail": "Invalid merchant_order_id"}, status=400)
    

    success = str(data.get('success')).lower()
    if success == 'true':
        print("Payment successful")
        get_order.order_status = "success"
        get_order.save()
        
        # Isn't allowed on Railway
        
#         message= f"""Hello {get_order.order_checkout.first_name},

# Thank you for your purchase!

# We’re happy to inform you that your payment with {int(data.get('amount_cents'))/100}EGP has been successfully processed.

# Your order is now being prepared. You will receive another email once it is shipped/ready.

# If you have any questions, feel free to contact us.

# Thank you for choosing us!
# """
        
        
#         send_mail(
#             "Furniture Payment",
#             message,
#             settings.EMAIL_HOST_USER,
#             [get_order.order_checkout.email],
#             fail_silently=False,
#         )
#         get_order.save()

        return redirect('products:home')
    
    else:
        print("Payment failed")
        get_order.order_status = "failed"
        get_order.save()
#         message= f"""Hello { get_order.order_checkout.first_name },

# Unfortunately, we were unable to process your payment for the following order:

# Please try again using a different payment method or contact your bank to resolve the issue.

# You can retry payment anytime from your account orders page.

# If you need help, we’re always here for you.
# """
#         send_mail(
#             "Furniture Payment",
#             message,
#             settings.EMAIL_HOST_USER,
#             [get_order.order_checkout.email],
#             fail_silently=False,
#         )

        
        return redirect('products:home')

