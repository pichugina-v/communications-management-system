from rest_framework import serializers

from django_layer.users.models import User


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", 'full_name', 'email', "phone", "password", "status", "department", "preferred_contact_method")
        extra_kwargs = {"password": {"write_only": True}}


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", 'full_name', 'email', "phone", "status", "department", "preferred_contact_method")
