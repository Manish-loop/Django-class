from django.urls import path
# from teacher.views import delete_teacher, list_class, teacher,teacher_create,modelform,teacher_update
from teacher.views import *

urlpatterns = [
    path('test',teacher,name="teacher-list"),
    path('create',teacher_create,name="teacher-create"),
    path('modelform/create',modelform,name="teacher-model-create"),
    path('edit/<id>',teacher_update,name="teacher-update"),
    path('delete/<id>',delete_teacher,name="teacher-delete"),
    
    # class url
    path('class',list_class,name="list_of_class"),
    path('class-create',create_class, name="create-class")
]

# school_url = [

# ]

# urlpatterns = school_url+teacher_url

# /teacher/test/hello/class/math <==> teacher-model-create

