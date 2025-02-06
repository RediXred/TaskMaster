from django.shortcuts import render
from .models import Task
from .serializer import TaskSerializer
from rest_framework import viewsets
# Create your views here.


class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer