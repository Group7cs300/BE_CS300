from rest_framework.viewsets import ModelViewSet

from course.models.course import Course
from course.serializers.course import CourseSerializer


class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
