from django import forms
from .models import Product
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# class StaffForm(forms.ModelForm):
#     class Meta:
#         model = Staff
#         fields = [ 'name', 'age', 'gender', 'birthday', 'image', 'address']

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [ 'username', 'email', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

