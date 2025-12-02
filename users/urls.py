from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/reset-password/', views.reset_password, name='reset_password'),
    path('accounts/signup/', views.signup_view, name='signup'),
]
