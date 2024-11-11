from django.urls import path
from user.views import *

urlpatterns = [
    path('login',user_login, name="login"),
    path('register',user_register, name="register"),
]