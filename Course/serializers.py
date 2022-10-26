from rest_framework import serializers

from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'date_upload','time_limit','state','tutor_id','price', 'cover_image','hashtag']
