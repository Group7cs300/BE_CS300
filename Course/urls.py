
from django.urls import path

from . import views
from django.conf import settings
urlpatterns = [
    path('', views.get_course, name="course_id"),
    path('update/<int:tutor_id>/<int:course_id>/', views.update, name="update_course")
]

