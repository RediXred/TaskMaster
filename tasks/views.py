from django.shortcuts import render
from .models import Task
from .serializer import TaskSerializer
from rest_framework import viewsets

from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializer import RegisterSerializer, LoginSerializer
# Create your views here.


class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]  # Открытый доступ

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer
