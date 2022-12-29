from rest_framework import serializers

from course.models.category import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'uuid','creater','created_by_system']
