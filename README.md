# Furniture E-Commerce Platform

## A Full-Stack Django Store with Cart, Orders, Payments, and Admin Management With Scalable Backend Structure

This project is a full-featured Furniture E-Commerce Platform built with Django, designed to demonstrate real-world backend engineering using modern, production-ready technologies. It includes a complete REST API, PostgreSQL database, Redis caching, authentication & authorization, and a fully functional payment integration, making it ideal for learning, showcasing your skills, or serving as a starter template for an actual online store.

To enhance performance and scalability, the project uses WhiteNoise for static file serving, Cloudinary for media storage, and Redis to optimize cart, sessions, and API performance. It also includes email notifications via Django Gmail SMTP, robust order management, secure checkout flow, and admin-friendly product management.

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
└── README.md               # Project documentation
