from rest_framework import serializers

from course.models.course import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class AutoCompleteCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name']