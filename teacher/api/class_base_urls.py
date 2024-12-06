from django.urls import path
from teacher.api.class_views import SerchClassView, TeacherView, SchoolClassView
urlpatterns = [
    path('',TeacherView.as_view(), name="techer-clas"),
    path('class',SchoolClassView.as_view(), name="techer-clas"),
    path('search',SerchClassView.as_view(), name="techer-class")
]