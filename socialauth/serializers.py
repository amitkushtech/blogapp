from atexit import register
from http import server
from re import L
from rest_framework.exceptions import AuthenticationFailed
import os
from rest_framework import serializers

from .register import register_socialuser
from . import facebook
from socialauth.facebook import Facebook


class FacebookSocialAuthSerializer(serializers.Serializer):
    auth_token = serializers.CharField()

    def validated_auth_token(self, auth_token):
        user_data = facebook.Facebook.validate(auth_token)
        try:
            user_id = user_data["id"]
            email = user_data["email"]
            name = user_data["name"]
            provider = "facebook"
            return register_socialuser(
                provider=provider, user_id=user_id, email=email, name=name
            )

        except Exception as e:
            raise serializers.ValidationError("The token is invalid or expired.")
