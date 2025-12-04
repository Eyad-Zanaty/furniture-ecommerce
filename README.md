# Furniture E-Commerce Platform

## A Full-Stack Django Store with Cart, Orders, Payments, and Admin Management With Scalable Backend Structure

This project is a full-featured Furniture E-Commerce Platform built with Django, designed to demonstrate real-world backend engineering using modern, production-ready technologies. It includes a complete REST API, PostgreSQL database, Redis caching, authentication & authorization, and a fully functional payment integration, making it ideal for learning, showcasing your skills, or serving as a starter template for an actual online store.

To enhance performance and scalability, the project uses WhiteNoise for static file serving, Cloudinary for media storage, and Redis to optimize cart, sessions, and API performance. It also includes email notifications via Django Gmail SMTP, robust order management, secure checkout flow, and admin-friendly product management.


furniture-ecommerce/
│
├── manage.py
├── requirements.txt
├── Dockerfile
│
├── project/                # Django project root (settings, urls, wsgi/asgi)
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── users/                  # App for user authentication / user management
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py      # Using DRF
│   ├── views.py
│   ├── urls.py
│   └── (other files: permissions, etc.)
│
├── products/               # App for products catalog, categories, images
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── (maybe image handling, cloudinary integration)
│
├── payment/                # App or module for payment logic / order payment
│   ├── __init__.py
│   ├── payment logic files (e.g. payment handlers, integrations)
│   ├── models.py (if orders/payments stored)
│   ├── serializers.py / views.py / urls.py (if via API)
│   └── (other related modules)
│
├── apis/                   # For API endpoints (Django REST Framework)
│   ├── __init__.py
│   ├── maybe versioning or router configs
│   ├── urls.py
│   └── (other API-level configs)
│
├── static/                 # Static files (CSS / JS / images / frontend assets)
│   └── ...
│
├── staticfiles/            # Collected static files — for deployment (e.g. via WhiteNoise)
│   └── ...
│
├── templates/              # HTML templates (if you have any server-side rendered pages)
│   └── (base templates, emails, etc.)
│
├── media/                  # Media / uploaded files (e.g. product images) — before or after Cloudinary sync 
│   └── products_image/
│
└── README.md               # Project documentation
