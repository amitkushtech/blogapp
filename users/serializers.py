from rest_framework import serializers
from .models import CustomUser
from django.core.exceptions import ValidationError


class CustomUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"
        read_only_fields = (
            "groups",
            "user_permissions",
            "last_login",
            "auth_providers",
        )
