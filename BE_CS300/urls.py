from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.views import SpectacularSwaggerView
from rest_framework.routers import SimpleRouter

from app.views import HealthCheckView
from course.views.course import CourseViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('healthcheck/', HealthCheckView.as_view()),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui')
]

router = SimpleRouter(trailing_slash=False)
router.register(r'^course', CourseViewSet)

urlpatterns += router.urls
