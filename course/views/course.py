from django.db.models import Avg
from django.db.models.functions import Coalesce
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from course.models.course import Course
from course.serializers.course import CourseDetailSerializer
from course.serializers.course import CourseSerializer
from django_filters import rest_framework as filters


class CourseFilter(filters.FilterSet):
    class Meta:
        model = Course
        fields = {
            'name': ['icontains']
        }


class CoursePagination(PageNumberPagination):
    page_size = 9
    max_page_size = 100


class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all().annotate(rate=Coalesce(Avg('rating__star'), 0.0))
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CourseFilter
    pagination_class = CoursePagination

    def get_serializer_class(self):
        match self.action:
            case 'retrieve':
                return CourseDetailSerializer
            case _:
                return CourseSerializer
