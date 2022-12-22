from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from app.models import BaseModel
from course.models import Course


def get_section_path(instance, filename):
    return f'courses/' \
           f'{instance.course.tutor.username}__{instance.course.tutor.uuid}/' \
           f'{instance.course.name}__{instance.course.uuid}/' \
           f'{instance.name}__{instance.uuid}/{filename}'


class Section(BaseModel):
    name = models.CharField(max_length=250)
    course = models.ForeignKey(Course, related_name='sections', on_delete=models.CASCADE)
    sectionNum = models.IntegerField(default=1, validators=[MaxValueValidator(50), MinValueValidator(1)])
    document = models.FileField(upload_to=get_section_path, max_length=500)
    video = models.FileField(upload_to=get_section_path, max_length=500)
