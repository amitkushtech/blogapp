from django.shortcuts import render
from .serializers import CustomUserSerializers
from .models import CustomUser
from rest_framework import viewsets

# Create your views here.
class CustomUserViews(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializers
