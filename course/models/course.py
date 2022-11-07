from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models

from app.models import Account
from app.models import BaseModel
from course.models.category import Category


class Course(BaseModel):
    name = models.CharField(max_length=250)
    is_finished = models.BooleanField(default=False)
    tutor = models.ForeignKey(Account, related_name='courses', on_delete=models.CASCADE)
    price = models.IntegerField(default=1, validators=[MaxValueValidator(500), MinValueValidator(1)])
    cover_image = models.ImageField(upload_to='courses/covers', null=True)
    categories = models.ManyToManyField(Category, related_name='courses')

    def __str__(self):
        return self.name

