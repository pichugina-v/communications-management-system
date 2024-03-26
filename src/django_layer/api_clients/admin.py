from django.contrib import admin

from django_layer.api_clients.models import APIClient


@admin.register(APIClient)
class APIClientAdmin(admin.ModelAdmin):
    search_fields = ['app_name']
