from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.response import Response

from django_layer.communication_rules.models import DepartmentCommunicationRule
from django_layer.communication_rules.serializers import (
    DepartmentCommunicationRuleCreateSerializer,
    DepartmentCommunicationRuleSerializer,
)
from django_layer.users.models import Department


class DepartmentCommunicationRuleViewSet(viewsets.ModelViewSet):
    queryset = DepartmentCommunicationRule.objects.all()
    serializer_class = DepartmentCommunicationRuleSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return DepartmentCommunicationRuleCreateSerializer
        return self.serializer_class


class DepartmentCommunicationRuleByDepartmentViewSet(viewsets.GenericViewSet, RetrieveModelMixin):
    queryset = DepartmentCommunicationRule.objects.all()
    serializer_class = DepartmentCommunicationRuleSerializer
    lookup_field = 'department'

    @extend_schema(description='Получение правила коммуникации по департаменту')
    @action(methods=['get'], detail=True)
    def get_department_communication_rule(self, request, *args, **kwargs):
        department_name = request.kwargs.get('department_name')
        department = Department.objects.get(internal_name=department_name)
        rules = department.department_communication_rules
        return Response({'rules': rules})
