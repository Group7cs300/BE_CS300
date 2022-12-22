from rest_framework import serializers

from app.serializers.account import AccountSerializer
from course.models.course import Course


class CourseSerializer(serializers.ModelSerializer):
    rate = serializers.FloatField()
    popular = serializers.IntegerField()
    tutor = AccountSerializer()

    class Meta:
        model = Course
        depth = 1
        fields = '__all__'


class UploadCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(serializers.ModelSerializer):
    tutor = AccountSerializer()

    class Meta:
        model = Course
        depth = 2
        fields = '__all__'
