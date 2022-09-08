from re import I
from django.shortcuts import render
from .serializers import BlogCategorySerializers
from .models import BlogCategory
from rest_framework import viewsets

# Create your views here.
class BlogViewSet(viewsets.ModelViewSet):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializers
