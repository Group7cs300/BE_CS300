import django_filters
from django.db.models import Avg
from django.db.models import Count
from django.db.models.functions import Coalesce
from django_filters import rest_framework as filters
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.viewsets import ModelViewSet

from course.models.course import Course
from course.serializers.course import CourseDetailSerializer
from course.serializers.course import CourseSerializer
from course.serializers.course import UploadCourseSerializer


class CourseFilter(filters.FilterSet):
    created_at__gt = django_filters.DateFilter(field_name='created_at', lookup_expr='date__gte')
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    tutor = django_filters.CharFilter(field_name='tutor')
    category = django_filters.CharFilter(field_name='categories')

    class Meta:
        model = Course
        fields = [
            'name',
            'created_at__gt',
            'tutor',
            'category'
        ]


class CoursePagination(PageNumberPagination):
    page_size = 9
    max_page_size = 100


class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()\
        .annotate(rate=Coalesce(Avg('rating__star'), 0.0))\
        .annotate(popular=Count('ownedcourse__user_id'))
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filterset_class = CourseFilter
    ordering_fields = ['price', 'rate', 'popular']
    pagination_class = CoursePagination

    def get_serializer_class(self):
        match self.action:
            case 'create':
                return UploadCourseSerializer
            case 'retrieve':
                return CourseDetailSerializer
            case _:
                return CourseSerializer

    def get_queryset(self):
        match self.action:
            case 'popular':
                return self.queryset.prefetch_related('ownedcourse_set')\
                    .annotate(owned_count=Count('ownedcourse__user'))\
                    .order_by('-owned_count')
            case 'bought_courses':
                return self.queryset.filter(ownedcourse__user_id=self.request.user)
            case 'retrieve':
                return self.queryset.prefetch_related('sections')
            case _:
                return self.queryset

    @action(methods=['GET'], detail=False, permission_classes=[IsAuthenticated])
    def bought_courses(self, request: Request):
        return self.list(request)

    @action(detail=False, methods=['get'])
    def popular(self, request):
        return self.list(request)

