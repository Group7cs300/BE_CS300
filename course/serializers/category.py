from rest_framework import serializers

from app.serializers.account import AccountSerializer, NameUserSerializer
from course.models.category import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
