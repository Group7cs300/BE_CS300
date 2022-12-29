from rest_framework import serializers

from app.serializers.account import AccountSerializer
from course.models import Category
from course.models.course import Course
from course.serializers.category import CategorySerializer


class CourseSerializer(serializers.ModelSerializer):
    rate = serializers.FloatField()
    popular = serializers.IntegerField()
    tutor = AccountSerializer()

    class Meta:
        model = Course
        depth = 1
        fields = '__all__'


class UploadCourseSerializer(serializers.ModelSerializer):
    custom_categories = serializers.ListField(child=serializers.CharField(), required=False, max_length=1)

    def create(self, validated_data):
        custom_categories = validated_data.pop('custom_categories', [])
        custom_cats = []
        for cat in custom_categories:
            custom_cat = Category.objects.create(name=cat)
            custom_cats.append(custom_cat)
        categories = custom_cats + validated_data.pop('categories')
        course = Course.objects.create( **validated_data)
        course.categories.set(categories)
        return course

    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(serializers.ModelSerializer):
    tutor = AccountSerializer()

    class Meta:
        model = Course
        depth = 2
        fields = '__all__'
