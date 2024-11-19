from django.urls import path
from user.views import *

urlpatterns = [
    path('login',user_login, name="login"),
    path('register',user_register, name="register"),
    path('change_password',change_password, name="change_password"),
    path('info', user_list, name="user_list"),
]