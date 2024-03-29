from django.db import models
from course.models.course import Course
from app.models import Account
from app.models import BaseModel


class OwnedCourse(BaseModel):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
