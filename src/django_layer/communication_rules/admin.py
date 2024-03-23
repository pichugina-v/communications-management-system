from django.contrib import admin

from django_layer.communication_rules.models import DepartmentCommunicationRule


@admin.register(DepartmentCommunicationRule)
class UserAdmin(admin.ModelAdmin):
    pass
