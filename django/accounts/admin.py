# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ("email", "username", "type", "is_staff")
    search_fields = ("email", "username")
    ordering = ("email",)

    # Update fieldsets to only include existing fields
    fieldsets = UserAdmin.fieldsets + (
        ("Custom Fields", {"fields": ("type", "address", "phone", "is_verified")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Custom Fields", {"fields": ("email", "type", "address", "phone")}),
    )
