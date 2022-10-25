from django.db import models
import uuid
from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Course(models.Model):
    # id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    id = models.CharField(primary_key=True,max_length=250)
    name = models.CharField(max_length=250,null=True)
    #date_upload = models.DateField(default=date.today)
    #upload_id = models.UUIDField(default=uuid.uuid4, editable=False)
    # time_limit
    # state
    price = models.IntegerField(default=1,
                                validators=[MaxValueValidator(100), MinValueValidator(1)])
    cover_image = models.ImageField(upload_to='Course/file/covers',null=True)
    hashtag = models.CharField(max_length=250,null=True)

    def __str__(self):
        return self.id




