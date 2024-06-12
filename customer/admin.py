from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ['name', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active', 'is_customer', 'is_expert', 'is_manager']
    fieldsets = (
        (None, {'fields': ('name', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_customer', 'is_expert', 'is_manager', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'created_at', 'updated_at')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ['name']
    ordering = ['name']  # Change to a valid field
    readonly_fields = ['created_at', 'updated_at']

admin.site.register(CustomUser, CustomUserAdmin)