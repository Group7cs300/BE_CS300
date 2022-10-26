from django.db import models
import uuid
from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Course(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=250, null=True)
    date_upload = models.DateField(default=date.today)
    time_limit = models.IntegerField(default=1,
                                     validators=[MaxValueValidator(180), MinValueValidator(0)])
    # State choice
    FINISHED = 'F'
    UPDATING = 'U'

    state_choices = [(FINISHED, 'Finished'), (UPDATING, 'Updating')]
    state = models.CharField(max_length=1,
                             choices=state_choices,
                             default=UPDATING)
    tutor_id = models.IntegerField(null=True)
    price = models.IntegerField(default=1,
                                validators=[MaxValueValidator(500), MinValueValidator(1)])
    cover_image = models.ImageField(upload_to='Course/file/covers', null=True)
    hashtag = models.CharField(max_length=250, null=True)


