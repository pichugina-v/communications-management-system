from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.mixins import RetrieveModelMixin

from django_layer.communication_rules.models import DepartmentCommunicationRule
from django_layer.communication_rules.serializers import DepartmentCommunicationRuleSerializer, \
    DepartmentCommunicationRuleCreateSerializer
from django_layer.users.models import Department


# @extend_schema_view(
#     get_deprtment_communication_rule=extend_schema(description='text')
# )
class DepartmentCommunicationRuleViewSet(viewsets.ModelViewSet):
    queryset = DepartmentCommunicationRule.objects.all()
    serializer_class = DepartmentCommunicationRuleSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return DepartmentCommunicationRuleCreateSerializer
        return self.serializer_class

class DepartmentCommunicationRuleByDepartmentViewSet(viewsets.GenericViewSet, RetrieveModelMixin):
    @extend_schema(description="Получение правила коммуникации по департаменту")
    @action(methods=["get"], detail=True)
    def get_department_communication_rule(self, request, *args, **kwargs):
        department_id = request.query_params.get('department_id')
        department = Department.objects.get(pk=department_id)
        rules = department.department_communication_rules
        return Response({"rules": rules})
