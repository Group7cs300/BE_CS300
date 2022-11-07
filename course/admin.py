from django.contrib import admin
from .models import Course, Section, Category, OwnedCourse


admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Category)
admin.site.register(OwnedCourse)
