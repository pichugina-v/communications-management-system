from django.urls import path

from django_layer.communication_statistics.api import StatisticsAPI

urlpatterns = [
    path('statistics/', StatisticsAPI.as_view({'get': 'list'}), name='statistics'),
]
