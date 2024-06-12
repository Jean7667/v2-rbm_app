from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('name', 'password')  # Adjust fields as per your CustomUser model

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('name', 'password', 'is_active', 'is_staff', 'is_customer', 'is_expert', 'is_manager')  # Adjust fields as per your CustomUser model