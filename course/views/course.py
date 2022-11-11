from rest_framework.viewsets import ModelViewSet

from course.models.course import Course
from course.serializers.course import CourseSerializer, AutoCompleteCourseSerializer
from django_filters import rest_framework as filters
from rest_framework.response import Response
from rest_framework.decorators import action

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
    def get_queryset(self,request, pk=None):
        objs = Course.objects.filter(name__icontains=pk).values('name')
        serializer = AutoCompleteCourseSerializer(objs,many=True)
        return Response(serializer.data)



