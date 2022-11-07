from rest_framework.viewsets import ModelViewSet

from course.models.course import Course
from course.serializers.course import CourseSerializer
from django_filters import rest_framework as filters


class CourseFilter(filters.FilterSet):
    class Meta:
        model = Course
        fields = {
            'name': ['icontains']
        }


class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CourseFilter
