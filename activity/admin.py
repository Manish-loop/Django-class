from django.contrib import admin
from activity.models import UserActivity
# Register your models here.

@admin.register(UserActivity) 
class TeacherAdmin(admin.ModelAdmin):
    list_display=['user','user_agent','ip_address','modules','created_at'] 
    