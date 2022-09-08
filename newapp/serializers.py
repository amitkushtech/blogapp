from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import BlogCategory


class BlogCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = "__all__"
