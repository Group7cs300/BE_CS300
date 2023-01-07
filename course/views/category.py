import django_filters
from django.db.models import Q
from rest_framework.viewsets import ModelViewSet

from course.models.category import Category
from course.serializers.category import CategorySerializer
from django_filters import rest_framework as filters


class CategoryFilter(filters.FilterSet):
    name = django_filters.CharFilter(field_name='name')
    creater = django_filters.CharFilter(field_name='creater')
    created_by_system = django_filters.BooleanFilter(field_name='created_by_system')
    class Meta:
        model = Category
        fields = [
            'name',
            'creater',
            'created_by_system'
        ]


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.none()
    filterset_class = CategoryFilter

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Category.objects.filter(Q(creater=self.request.user) | Q(created_by_system=True))
        return Category.objects.filter(created_by_system=True)

