from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from app.models import Account
from app.models import BaseModel
from course.models import Course


class Rating(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    star = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(0)])
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
