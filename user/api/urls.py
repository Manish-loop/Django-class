from django.urls import path
from user.api.views import *

urlpatterns = [
    path('', user_info, name="user-info"),
    path('login', user_login, name="user-login"),
    
    
    path('register', user_register, name='register'),
    
]
