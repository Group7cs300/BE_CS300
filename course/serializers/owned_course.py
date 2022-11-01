from rest_framework import serializers

from course.models.owned_course import OwnedCourse


class OwnedCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnedCourse
        fields = '__all__'
