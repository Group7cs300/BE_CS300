from django.contrib.auth.models import AbstractUser

from app.models.base import BaseModel


class Account(BaseModel, AbstractUser):
    pass
