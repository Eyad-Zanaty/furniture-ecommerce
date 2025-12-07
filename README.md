# Furniture E-Commerce Platform

## A Full-Stack Django Store with Cart, Orders, Payments, and Admin Management With Scalable Backend Structure

This project is a full-featured Furniture E-Commerce Platform built with Django, designed to demonstrate real-world backend engineering using modern, production-ready technologies. It includes a complete REST API, PostgreSQL database, Redis caching, authentication & authorization, and a fully functional payment integration, making it ideal for learning, showcasing your skills, or serving as a starter template for an actual online store.

To enhance performance and scalability, the project uses WhiteNoise for static file serving, Cloudinary for media storage, and Redis to optimise cart, sessions, and API performance. It also includes email notifications via Django Gmail SMTP, robust order management, secure checkout flow, and admin-friendly product management.

## Technologies & Tools Used

- Django
- Django REST Framework (DRF)
- PostgreSQL
- Redis (caching for cart, sessions, and API performance)
- Authentication & Authorization (Django auth)
- Payment Integration: Paymob
- Cloudinary (media storage)
- WhiteNoise (static file serving)
- Django Gmail SMTP (email notifications)
- Docker
- Python 3.x
- frontend template
- Git / GitHub (version control)
- Docker Compose (if used for local setup)

## 📦 API Endpoints Diagram

### 🛒 Products API
/products/                 → GET (List Products)  
/products/                 → POST (Create Product)  
/products/<id>/            → PUT (Update Product)  
/products/<id>/            → DELETE (Delete Product)

### 👤 Users API (Admin Only)
/users/                    → GET (List Users)  
/users/                    → POST (Create User)  
/users/<id>/               → GET (Retrieve User)  
/users/<id>/               → PUT (Update User)  
/users/<id>/               → DELETE (Delete User)

### 🛍 Cart API
/cart/                     → GET (List Cart Items)  
/cart/                     → POST (Add to Cart)  
/cart/<id>/                → GET (Retrieve Cart Item)  
/cart/<id>/                → PUT (Update Cart Item)  
/cart/<id>/                → DELETE (Delete Cart Item)

### 💳 Checkout API
/checkout/                 → GET (List Checkouts)  
/checkout/                 → POST (Create Checkout Session)  
/checkout/<id>/            → GET (Retrieve Checkout)  
/checkout/<id>/            → PUT (Update Checkout)  
/checkout/<id>/            → DELETE (Delete Checkout)

### 📦 Orders API
/orders/                   → GET (List Orders)  
/orders/                   → POST (Create Order)  
/orders/<id>/              → GET (Retrieve Order)  
/orders/<id>/              → PUT (Update Order)  
/orders/<id>/              → DELETE (Delete Order)

![alt text](/landpage-screenshot.jpg])

```

## 📁 Project Structure

```plaintext
furniture-ecommerce/
│
├── manage.py
├── requirements.txt
├── Dockerfile
│
├── project/                     # Django project root (settings, urls, wsgi/asgi)
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── users/                       # Authentication & User Management
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── permissions.py (if any)
│
├── products/                    # Products, Categories, Images
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── cloudinary handlers (if any)
│
├── payment/                     # Payment integration logic
│   ├── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── payment handlers / gateways
│
├── apis/                        # API endpoints structure
│   ├── __init__.py
│   ├── urls.py
│   └── routers / versioning
│
├── static/                      # Static assets
│   └── ...
│
├── staticfiles/                 # Collected static files (for WhiteNoise)
│   └── ...
│
├── templates/                   # Email & HTML templates
│   └── ...
│
├── media/                       # Uploaded media
│   └── products_image/
│
└── README.md                    # Project documentation

```


