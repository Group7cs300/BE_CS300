from rest_framework.views import APIView
from rest_framework.response import Response
from course.models import *


class Rating(APIView):
    def get(self, request):
        all_rating = Rating.objects.all().values()
        return Response({"Message": "List of rating", "Rating": all_rating})

    def post(self, request):
        new_rating = Rating.objects.create(course=request.data["course"],
                              star=request.data["star"],
                              user=request.data["user"])
        return Response({"Message": "New Rating added!", "Rating": new_rating})
