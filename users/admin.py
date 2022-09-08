from django.contrib import admin
from .models import *

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "is_active",
        "is_staff",
        "is_superuser",
        "user_type",
        "date_joined",
    )


admin.site.register(CustomUser, CustomUserAdmin)
