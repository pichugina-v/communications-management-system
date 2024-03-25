from rest_framework import viewsets

from django_filters import rest_framework as filters
from django_layer.users.models import Department, User
from django_layer.users.serializers import DepartmentCreateSerializer, DepartmentSerializer, UserSerializer, UserCreateSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('status', )

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        return self.serializer_class


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return DepartmentCreateSerializer
        return self.serializer_class
