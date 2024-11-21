from django.urls import path
from teacher.api.views import teacher_list,teacher_first, teacher_add, teacher_update,teacher_delete

urlpatterns = [
    path('',teacher_list, name="teacher-info"),
    path('first',teacher_first ,name="teacher-first"),
    path('add',teacher_add ,name="teacher-add"),
    path('update/<int:id>',teacher_update, name="teacher-update"),
    path('delete/<int:id>',teacher_delete, name="teacher-delete"),
    
] 