from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(models.Model):
    location = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)

    is_customer = models.BooleanField(default=False)
    is_expert = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


