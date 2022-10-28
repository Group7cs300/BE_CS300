from rest_framework.viewsets import ModelViewSet

from section.models import Section
from section.serializers.section import SectionSerializer


class SectionViewSet(ModelViewSet):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()