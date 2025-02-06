from django.shortcuts import render
from .models import Task
from .serializer import TaskSerializer
from rest_framework import viewsets

from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializer import RegisterSerializer, LoginSerializer
from django.core.cache import cache
# Create your views here.


class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        task = serializer.save(owner=self.request.user)
        cache.set(f'task_{self.request.user.id}_{task.id}', task, timeout=3600)

    def retrieve(self, request, *args, **kwargs):
        task_id = kwargs.get('pk')
        cached_task = cache.get(f'task_{self.request.user.id}_{task_id}')
        if cached_task:
            serializer = self.get_serializer(cached_task)
            return Response(serializer.data)
        else:
            task = self.get_object()
            cache.set(f'task_{self.request.user.id}_{task_id}', task, timeout=3600)
            serializer = self.get_serializer(task)
            return Response(serializer.data)
    
    def perform_update(self, serializer):
        task = serializer.save()
        cache.delete(f'task_{self.request.user.id}_{task.id}')
        cache.set(f'task_{self.request.user.id}_{task.id}', task, timeout=3600)
    
    def perform_destroy(self, instance):
        cache.delete(f'task_{self.request.user.id}_{instance.id}')
        instance.delete()
            
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]  # Открытый доступ

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer
