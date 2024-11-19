from django.urls import path
from teacher.api.views import teacher_list

urlpatterns = [
    path('',teacher_list, name="teacher-info"),
]