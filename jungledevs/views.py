from django.shortcuts import render
from django.contrib.auth.models import User
from jungledevs.api.serializers import RegisterSerializer
from rest_framework import generics

# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
