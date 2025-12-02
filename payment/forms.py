from django import forms
from .models import checkout, checkout_country_choices

class CheckoutForm(forms.ModelForm):
    checkout_firstname = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control', 'id': 'first_name'}))
    checkout_lastname = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control', 'id': 'last_name'}))
    checkout_company_name = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': 'Company Name', 'class': 'form-control', 'id': 'company'}))
    checkout_email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control', 'id': 'email'}))
    checkout_country = forms.ChoiceField(choices=checkout_country_choices, required=True, widget=forms.Select(attrs={'class': 'w-100', 'id': 'country'}))
    checkout_town = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'placeholder': 'Town', 'class': 'form-control', 'id': 'city'}))
    checkout_address = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'placeholder': 'Address', 'class': 'form-control mb-3', 'id': 'street_address'}))
    checkout_zipcode = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'placeholder': 'Zip Code', 'class': 'form-control', 'id': 'zip_code'}))
    checkout_phone_number = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'placeholder': 'Phone No', 'class': 'form-control', 'id': 'phone_number', 'min': '0'}))
    checkout_order_comment = forms.CharField(required=False, widget=forms.Textarea(attrs={'placeholder': 'Leave a comment about your order', 'class': 'form-control w-100', 'id': 'comment', 'cols': '30', 'rows': '10', 'name': 'comment'}))
    checkout_create_account = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'id': 'customCheck2', 'class': 'custom-control-input', 'label': 'Create an account?', 'for': 'customCheck2'}))    
    
    class Meta:
        model = checkout
        fields = [
            'checkout_firstname',
            'checkout_lastname',
            'checkout_company_name',
            'checkout_email',
            'checkout_country',
            'checkout_town',
            'checkout_address',
            'checkout_zipcode',
            'checkout_phone_number',
            'checkout_order_comment',
            'checkout_create_account',
        ]