from rest_framework import viewsets
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin

from django_layer.communication_rules.models import DepartmentCommunicationRule
from django_layer.communication_rules.serializers import (
    DepartmentCommunicationRuleCreateSerializer,
    DepartmentCommunicationRuleSerializer,
)


class DepartmentCommunicationRuleViewSet(viewsets.ModelViewSet):
    queryset = DepartmentCommunicationRule.objects.all()
    serializer_class = DepartmentCommunicationRuleSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return DepartmentCommunicationRuleCreateSerializer
        return self.serializer_class


class DepartmentCommunicationRuleByDepartmentViewSet(viewsets.GenericViewSet, RetrieveModelMixin, UpdateModelMixin):
    queryset = DepartmentCommunicationRule.objects.all()
    serializer_class = DepartmentCommunicationRuleSerializer
    lookup_field = 'department'
