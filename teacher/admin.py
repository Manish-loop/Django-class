from django.contrib import admin
from teacher.models import Teacher, SchoolClass
# Register your models here.
# admin.site.register(Teacher) # First approach

@admin.register(Teacher) 
class TeacherAdmin(admin.ModelAdmin):
    list_display=['name','email','created_at'] 
    search_fields=['name']
    list_filters=['is_active']
    list_per_page=20
    
@admin.register(SchoolClass) 
class SchoolClassAdmin(admin.ModelAdmin):
    list_display=['name','created_at'] 
    search_fields=['name']
    autocomplete_fields = ['teacher']
    list_filters=['is_active']
    list_per_page=20