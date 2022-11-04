from rest_framework.viewsets import ModelViewSet

from course.models.owned_course import OwnedCourse
from course.serializers.owned_course import OwnedCourseSerializer
from django_filters import rest_framework as filters


class OwnedCourseViewSet(ModelViewSet):
    serializer_class = OwnedCourseSerializer
    queryset = OwnedCourse.objects.all()
