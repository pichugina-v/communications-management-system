from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema
from rest_framework.mixins import ListModelMixin

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

class CommunicationMethodsViewSet(viewsets.GenericViewSet, ListModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @extend_schema(description="Получение методы коммуникации по пользователю")
    @action(methods=["get"], detail=False)
    def get_user_communication_methods(self, request, *args, **kwargs):
        methods = User().CONTACT_METHODS
        return Response({"methods": methods})
