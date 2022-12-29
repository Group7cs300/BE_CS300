from rest_framework.viewsets import ModelViewSet

from course.models import Section
from course.serializers.section import SectionSerializer


class SectionViewSet(ModelViewSet):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()