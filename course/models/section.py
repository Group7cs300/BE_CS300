from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from app.models import BaseModel
from course.models import Course


# Create your models here.

class Section(BaseModel):
    name = models.CharField(max_length=250)

    course = models.ForeignKey(Course, related_name='sections', on_delete=models.CASCADE)

    sectionNum = models.IntegerField(default=1, validators=[MaxValueValidator(50), MinValueValidator(1)])
    document = models.CharField(max_length=500)
    video = models.FileField(upload_to="sections/video")