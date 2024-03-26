from rest_framework import serializers

from django_layer.users.models import Department, User


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'full_name', 'email', 'phone', 'password', 'status', 'department', 'preferred_contact_method')
        extra_kwargs = {'password': {'write_only': True}}


class UserSerializer(serializers.ModelSerializer):
    department = serializers.CharField(source='department.name', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'full_name', 'email', 'phone', 'status', 'department', 'preferred_contact_method')


class DepartmentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
