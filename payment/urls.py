
from .views import checkout_view
from .api import create_payment, payment_callback
from django.urls import path

app_name= "payment"
urlpatterns = [
    path('', checkout_view, name='checkout'),
    path("paymob/create/", create_payment, name='paymob'),
    path("paymob/webhook/", payment_callback),
]