from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    USER_TYPES = (("Admin", "Admin"), ("Writer", "Writer"), ("Reader", "Reader"))
    email = models.EmailField(_("email address"), unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    user_type = models.CharField(max_length=30, choices=USER_TYPES)
    date_joined = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = "email"

    objects = CustomUserManager()

    def __str__(self):
        return self.email


    
