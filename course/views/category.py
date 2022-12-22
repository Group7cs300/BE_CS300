from rest_framework.viewsets import ModelViewSet

from course.models.category import Category
from course.serializers.category import CategorySerializer


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
