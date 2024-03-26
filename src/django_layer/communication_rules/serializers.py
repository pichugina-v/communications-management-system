from rest_framework import serializers

from django_layer.communication_rules.models import DepartmentCommunicationRule


class DepartmentCommunicationRuleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentCommunicationRule
        fields = ('id', 'department', 'communication_limit', 'preferred_mass_channels',
                  'preferred_personal_channels')
        read_only_fields = ('id', 'created_at', 'updated_at')


class DepartmentCommunicationRuleSerializer(serializers.ModelSerializer):
    department = serializers.CharField(source='department.internal_name', read_only=True)

    class Meta:
        model = DepartmentCommunicationRule
        fields = ('id', 'department', 'communication_limit', 'preferred_mass_channels',
                  'preferred_personal_channels', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')
