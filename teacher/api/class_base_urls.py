from django.urls import path
from teacher.api.class_views import TeacherView, SchoolClassView
urlpatterns = [
    path('',TeacherView.as_view(), name="techer-clas"),
    path('class',SchoolClassView.as_view(), name="techer-clas"),

]