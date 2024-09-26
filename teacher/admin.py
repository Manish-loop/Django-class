from django.contrib import admin
from teacher.models import Teacher
# Register your models here.
# admin.site.register(Teacher) # First approach

@admin.register(Teacher)  # Decorators
class TeacherAdmin(admin.ModelAdmin):
    list_display=['name'] 