from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from django_layer.communication_rules.models import DepartmentCommunicationRule
from django_layer.users.models import Department, User
from django_layer.users.serializers import (
    DepartmentCreateSerializer,
    DepartmentSerializer,
    UserCreateSerializer,
    UserSerializer,
)


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
    lookup_field = 'internal_name'

    def get_serializer_class(self):
        if self.action == 'create':
            return DepartmentCreateSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        instance = serializer.save()
        DepartmentCommunicationRule.objects.create(department=instance)


class PreferredContactMethodAPI(APIView):
    def get(self, request):
        preferred_contact_methods = [method[0] for method in User.CONTACT_METHODS]
        return Response(preferred_contact_methods)
