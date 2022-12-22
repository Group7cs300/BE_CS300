import django_filters
from django.db.models import Avg, Count
from django.db.models.functions import Coalesce
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from course.models.course import Course
from course.serializers.course import CourseDetailSerializer, UploadCourseSerializer
from course.serializers.course import CourseSerializer
from django_filters import rest_framework as filters


class CourseFilter(filters.FilterSet):
    updated_at__gt = django_filters.DateFilter(field_name='updated_at', lookup_expr='date__gte')
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Course
        fields = [
            'name',
            'updated_at__gt'
        ]

class CoursePagination(PageNumberPagination):
    page_size = 9
    max_page_size = 100


class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all().annotate(rate=Coalesce(Avg('rating__star'), 0.0)).annotate(popular=Count('ownedcourse__user_id'))
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filterset_class = CourseFilter
    ordering_fields = ['price','rate','popular']
    pagination_class = CoursePagination

    def get_serializer_class(self):
        match self.action:
            case 'create':
                return UploadCourseSerializer
            case 'retrieve':
                return CourseDetailSerializer
            case _:
                return CourseSerializer
