from django.contrib import admin

# Register your models here.
from .models import Course
from .models import OwnedCourse
# Register your models here.

admin.site.register(Course)
admin.site.register(OwnedCourse)
