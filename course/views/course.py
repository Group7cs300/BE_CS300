from django.db.models import Count, Prefetch
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from course.models.course import Course
from course.models.rating import Rating
from course.models.owned_course import OwnedCourse
from course.serializers.course import CourseSerializer, CourseNameSerializer
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

    @action(detail=True, methods=['get'])
    def get_category_course(self, request, pk=None):
        objs = Course.objects.filter(categories__name__icontains=pk).values('name')
        serializer = CourseNameSerializer(objs, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def get_popular_course(self, request, pk=None):
        prefetch = Prefetch('course_id', queryset=Course.objects.all())  # point primary key
        objs = OwnedCourse.objects.prefetch_related(prefetch).filter(course_id__categories__name__icontains=pk)
        objs = objs.values_list('course_id__name').annotate(num_owendcourse=Count('user_id')).order_by('-num_owendcourse')
        b = [obj[0] for obj in objs]
        c = Course.objects.filter(name__in=b)
        serializer = CourseNameSerializer(c, many=True)
        return Response(serializer.data)
