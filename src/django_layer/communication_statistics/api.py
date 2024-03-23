from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.response import Response

from django_layer.communication_statistics.mocks import MOCKED_STATISTICS
from django_layer.communication_statistics.serializers import StatisticsSerializer


class StatisticsAPI(viewsets.ModelViewSet):
    @extend_schema(
        parameters=[StatisticsSerializer],
        request=StatisticsSerializer,
    )
    def list(self, request, *args, **kwargs):
        statistics = MOCKED_STATISTICS
        return Response(statistics)
