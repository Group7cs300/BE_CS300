from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from course.models import Course
from course.serializers.category import CategorySerializer
from course.models.category import Category
from course.serializers.course import CourseNameSerializer


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    @action(detail=False, methods=['get'])
    def get_category_course(self, request, pk=None):
        objs = Course.objects.filter(categories__name__icontains=pk).values('name')
        serializer = CourseNameSerializer(objs, many=True)
        return Response(serializer.data)
