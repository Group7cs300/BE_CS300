from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.views import SpectacularSwaggerView
from rest_framework.routers import SimpleRouter

from app.utils.environment import is_local
from app.views.health_check import HealthCheckView
from course.views.category import CategoryViewSet
from course.views.course import CourseViewSet
from course.views.owned_course import OwnedCourseViewSet
from course.views.section import SectionViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('healthcheck/', HealthCheckView.as_view()),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('app/', include('app.urls')),
]

if is_local():
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

router = SimpleRouter(trailing_slash=False)
router.register(r'^course', CourseViewSet)
router.register(r'^owned_courses', OwnedCourseViewSet)
router.register(r'^categories', CategoryViewSet)
router.register(r'^sections', SectionViewSet)

urlpatterns += router.urls
