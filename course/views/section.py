from django_filters import rest_framework as filters
from rest_framework.viewsets import ModelViewSet
import django_filters
from course.models import Section
from course.serializers.section import SectionSerializer
from rest_framework.filters import OrderingFilter


class SectionFilter(filters.FilterSet):
    course = django_filters.CharFilter(field_name='course')

    class Meta:
        model = Section
        fields = [
            'course',
        ]


class SectionViewSet(ModelViewSet):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filterset_class = SectionFilter
    ordering_fields = ['sectionNum']
