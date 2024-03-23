from rest_framework import viewsets

from django_layer.communication_rules.models import DepartmentCommunicationRule
from django_layer.communication_rules.serializers import DepartmentCommunicationRuleSerializer, \
    DepartmentCommunicationRuleCreateSerializer


class DepartmentCommunicationRuleViewSet(viewsets.ModelViewSet):
    queryset = DepartmentCommunicationRule.objects.all()
    serializer_class = DepartmentCommunicationRuleSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return DepartmentCommunicationRuleCreateSerializer
        return self.serializer_class
