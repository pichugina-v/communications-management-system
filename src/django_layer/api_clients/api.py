import secrets
from datetime import datetime, timedelta

from rest_framework import viewsets

from django_layer.api_clients.models import APIClient
from django_layer.api_clients.serializers import APIClientCreateSerializer, APIClientSerializer


class APIClientViewSet(viewsets.ModelViewSet):
    queryset = APIClient.objects.all()
    serializer_class = APIClientSerializer

    def perform_create(self, serializer: APIClientCreateSerializer):
        access_datetime = datetime.now() + timedelta(days=7)
        client_secret = secrets.token_urlsafe(16)
        serializer.save(access_datetime=access_datetime, client_secret=client_secret)

    def get_serializer_class(self):
        if self.action == 'create':
            return APIClientCreateSerializer
        return self.serializer_class
