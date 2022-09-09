from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.

AUTH_PROVIDERS = {"facebook": "facebook", "email": "email"}


class CustomUser(AbstractBaseUser, PermissionsMixin):
    USER_TYPES = (("Admin", "Admin"), ("Writer", "Writer"), ("Reader", "Reader"))
    username = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(_("email address"), unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    user_type = models.CharField(max_length=30, choices=USER_TYPES)
    date_joined = models.DateTimeField(default=timezone.now)
    auth_providers = models.CharField(
        max_length=20, blank=True, null=True, default=AUTH_PROVIDERS.get("email")
    )
    USERNAME_FIELD = "email"

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {"refresh": str(refresh), "access": str(refresh.access_token)}
