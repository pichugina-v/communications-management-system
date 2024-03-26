from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('django_layer.api_clients.urls')),
    path('api/', include('django_layer.users.urls')),
    path('api/', include('django_layer.communication_rules.urls')),
    path('api/', include('django_layer.communication_statistics.urls')),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
