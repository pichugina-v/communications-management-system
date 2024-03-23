from django.urls import path

from django_layer.communication_rules.api import DepartmentCommunicationRuleViewSet

urlpatterns = [
    path('communication-rules/', DepartmentCommunicationRuleViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='communication-rules-list-create'),
    path('communication-rules/<int:pk>/',
         DepartmentCommunicationRuleViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='communication-rules-detail-update-delete'),
]
