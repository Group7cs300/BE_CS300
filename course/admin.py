from django.contrib import admin
from .models import Course, Section
from .models import OwnedCourse
from .models.category import Category

# Register your models here.

admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Category)
admin.site.register(OwnedCourse)
