from django.shortcuts import render
from rest_framework import generics

from rest_framework_simplejwt.views import TokenObtainPairView

from userauths.models import User, Profile
from userauths.serializers import MyTokenObtainPairSerializer, RegisterSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
