from rest_framework import serializers

from course.models import Section


class SectionSerializer(serializers.ModelSerializer):
    document_name = serializers.ReadOnlyField(source='get_document_name')
    video_name = serializers.ReadOnlyField(source='get_video_name')
    class Meta:
        model = Section
        fields = '__all__'
