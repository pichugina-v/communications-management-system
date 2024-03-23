from rest_framework import viewsets

from django_filters import rest_framework as filters
from django_layer.users.models import User
from django_layer.users.serializers import UserSerializer, UserCreateSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('status', )

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        return self.serializer_class
