from rest_framework import serializers

from django_layer.api_clients.models import APIClient


class APIClientCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = APIClient
        fields = ("id", 'app_name', 'description', "client_secret", "access_datetime")
        read_only_fields = ("id", "client_secret", "access_datetime")


class APIClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = APIClient
        fields = ("id", 'app_name', 'description', "access_datetime")
        read_only_fields = ("id", "access_datetime")
