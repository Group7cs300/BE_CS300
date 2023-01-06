from rest_framework import serializers

from course.models.rating import Rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class PostRatingSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = validated_data.pop('user')
        course = validated_data.pop('course')
        star = validated_data.pop('star')
        obj, created = Rating.objects.update_or_create(user=user, course=course, defaults={'star': star})
        return obj

    class Meta:
        model = Rating
        fields = '__all__'
