from rest_framework.decorators import api_view

from .models import Course
from .serializers import CourseSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse


# Create your views here.

@api_view(['GET','POST'])
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
