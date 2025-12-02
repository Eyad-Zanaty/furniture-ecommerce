from django.shortcuts import render
from .models import CustomUser as User
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.

def login_view(request):
    if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            
            user= authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'products/home.html', {'message': 'Login successful'})
            else:
                error= 'Invalid email or password'
                return render(request, 'users/login_page.html', {"error":error})

    return render(request, 'users/login_page.html')


def signup_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        company_name = request.POST.get('company_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 != password2:
            error= 'Passwords do not match'
            return render(request, 'users/signup_page.html', {"error":error})
        
        if User.objects.filter(email=email).exists():
            error= 'Email already registered'
            return render(request, 'users/signup_page.html', {"error": error})
        
        User.objects.create_user(email=email, password=password1, first_name=first_name, last_name=last_name,
                                 company_name=company_name, phone_number=phone_number, address=address)
        messages.success(request, 'Signup successful. Please log in.')
        return render(request, 'users/login_page.html')
    
    return render(request, 'users/signup_page.html')


def reset_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_new_password = request.POST.get('confirm_new_password')
        
        if new_password != confirm_new_password:
            messages.error(request, 'New passwords do not match')
            return render(request, 'users/reset_password_page.html')
        
        user= authenticate(request, email=email, password=old_password)
        if user is not None:
            user.set_password(new_password)
            user.save()
            messages.success(request, 'Password reset successful')
            return render(request, 'users/login_page.html')
        else:
            error= 'Invalid email or password'
            return render(request, 'users/reset_password_page.html', {"error": error})
    
    return render(request, 'users/reset_password_page.html')