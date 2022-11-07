from rest_framework.viewsets import ModelViewSet

from course.models.owned_course import OwnedCourse
from course.serializers.owned_course import OwnedCourseSerializer


class OwnedCourseViewSet(ModelViewSet):
    serializer_class = OwnedCourseSerializer
    queryset = OwnedCourse.objects.all()
