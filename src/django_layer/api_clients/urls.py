from django.urls import path

from django_layer.api_clients.api import APIClientViewSet

urlpatterns = [
    path('clients/', APIClientViewSet.as_view({'get': 'list', 'post': 'create'}), name='clients-list-create'),
    path('clients/<int:pk>/', APIClientViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='clients-detail'),
]
