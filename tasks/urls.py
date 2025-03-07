from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskView, RegisterView, LoginView

router = DefaultRouter()
router.register(r"tasks", TaskView, basename="tasks")

urlpatterns = [
    path("", include(router.urls)),
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
]
