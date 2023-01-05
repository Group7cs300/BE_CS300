import django_filters
from django.db.models import Q
from rest_framework.viewsets import ModelViewSet

from course.models import Rating
from course.models.category import Category
from course.serializers.category import CategorySerializer
from django_filters import rest_framework as filters

from course.serializers.rating import RatingSerializer, PostRatingSerializer


class RatingFilter(filters.FilterSet):
    user = django_filters.CharFilter(field_name='user')
    course = django_filters.CharFilter(field_name='course')
    class Meta:
        model = Rating
        fields = [
            'user',
            'course'
        ]


class RatingViewSet(ModelViewSet):
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()
    filterset_class = RatingFilter

    def get_serializer_class(self):
        match self.action:
            case 'create':
                return PostRatingSerializer
            case _:
                return RatingSerializer



