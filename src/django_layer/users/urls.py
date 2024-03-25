from django.urls import path

from django_layer.users.api import CommunicationMethodsViewSet, DepartmentViewSet, UserViewSet

urlpatterns = [
    path('users/', UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='clients-list-create'),
    path('users/<int:pk>/', UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='clients-detail-update-delete'), 
    path('departments/', DepartmentViewSet.as_view({'get': 'list', 'post': 'create'}), name='departments-list-create'),
    path('departments/<int:pk>/', DepartmentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='departments-detail-update-delete'),
    path('communication-methods/', CommunicationMethodsViewSet.as_view({'get': 'list'}),
         name='communication-methods-detail'), 
]
