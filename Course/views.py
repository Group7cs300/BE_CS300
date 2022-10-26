from rest_framework.decorators import api_view

from .models import Course
from .serializers import CourseSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse


# Create your views here.

@api_view(['GET', 'POST'])
def get_course(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        serializers = CourseSerializer(courses, many=True).data
        return Response(serializers)

    if request.method == 'POST':
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"invalid": "not good data"}, status=404)


@api_view(['PUT','DELETE'])
def update(request,tutor_id, course_id):
    try:
        course = Course.objects.filter(tutor_id=tutor_id,id=course_id).first()
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

