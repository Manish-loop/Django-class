from django.urls import path
from activity.api import views

urlpatterns = [
    path('activities/', views.user_activity_list, name='user_activity_list'), 
    # path('activities/first/', views.user_activity_first, name='user_activity_first'), 
    path('activities/add/', views.user_activity_add, name='user_activity_add'),  
    path('activities/update/<int:id>/', views.user_activity_update, name='user_activity_update'), 
    path('activities/delete/<int:id>/', views.user_activity_delete, name='user_activity_delete'),  
]
