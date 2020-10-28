from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    billing_address = forms.CharField(max_length=200)
    default_shipping_address = forms.CharField(max_length=200)
    country = forms.CharField(max_length=200)
    phone = forms.CharField(max_length=11, help_text='Optional.')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'billing_address', 'default_shipping_address', 'country', 'phone', 'password1', 'password2',)