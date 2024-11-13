from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.conf import settings
from restaurants.models import Restaurant


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("username", email)  # Set username to email

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    class UserType(models.TextChoices):
        ADMIN = "admin"
        CHEF = "chef"
        WAITER = "waiter"
        CUSTOMER = "customer"

    email = models.EmailField(unique=True)
    address = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    type = models.CharField(
        max_length=100, choices=UserType.choices, default=UserType.CUSTOMER
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_verified = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
