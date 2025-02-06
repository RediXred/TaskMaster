from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        from django.contrib.auth import authenticate
        
        user = authenticate(username=data["username"], password=data["password"])
        if not user:
            raise serializers.ValidationError("Wrong user data")

        refresh = RefreshToken.for_user(user)

        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }