from rest_framework import serializers

from course.models.course import Course


class CourseSerializer(serializers.ModelSerializer):
    rate = serializers.FloatField()
    popular = serializers.IntegerField()
    class Meta:
        model = Course
        depth = 1
        fields = '__all__'


class CourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        depth = 2
        fields = '__all__'
