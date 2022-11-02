from django.contrib import admin

# Register your models here.
from .models import Course, Section
from .models.category import Tag, Category

# Register your models here.

admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Category)
admin.site.register(Tag)