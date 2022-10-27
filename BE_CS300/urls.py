from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.views import SpectacularSwaggerView

from app.views import HealthCheckView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('healthcheck/', HealthCheckView.as_view()),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui')
]
