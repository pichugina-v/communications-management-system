from django.urls import path

from django_layer.users.api import UserViewSet

urlpatterns = [
    path('users/', UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='clients-list-create'),
    path('users/<int:pk>/', UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='clients-detail-update-delete'),
]
