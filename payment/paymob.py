import requests
from django.conf import settings


class Paymob:
    @staticmethod
    def get_auth_token():
        url = f"{settings.PAYMOB_BASE_URL}/auth/tokens"
        payload = {"api_key": settings.PAYMOB_API_KEY}
        return requests.post(url, json=payload).json()["token"]

    @staticmethod
    def create_order(auth_token, amount, merchant_order_id):
        url = f"{settings.PAYMOB_BASE_URL}/ecommerce/orders"
        payload = {
            "auth_token": auth_token,
            "delivery_needed": False,
            "amount_cents": amount,
            "currency": "EGP",
            "merchant_order_id": merchant_order_id,
            "items": []
        }
        return requests.post(url, json=payload).json()

    @staticmethod
    def get_payment_token(auth_token, paymob_order_id, amount, user):
        url = f"{settings.PAYMOB_BASE_URL}/acceptance/payment_keys"
        payload = {
        "auth_token": auth_token,
        "amount_cents": amount,
        "expiration": 3600,
        "order_id": paymob_order_id,
        "currency": "EGP",
        "integration_id": settings.PAYMOB_INTEGRATION_ID,
        "billing_data": {
            "apartment": "NA",
            "email": user.email,
            "floor": "NA",
            "first_name": user.first_name,
            "street": user.address or "NA",
            "building": "NA",
            "phone_number": user.phone_number or "NA",
            "shipping_method": "NA",
            "postal_code": "NA",
            "city": "NA",
            "country": "EG",
            "last_name": user.last_name,
            "state": "NA"
        }
        }
        return requests.post(url, json=payload).json()["token"]
