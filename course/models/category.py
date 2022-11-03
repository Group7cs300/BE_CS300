from django.db import models

from app.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=100, null=False, unique=True)
    created_by_system = models.BooleanField(default=False)


