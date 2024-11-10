"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home.views import test, json_test,temp_render ,home_render # home folder ko views.py file ko test function lai import garne 
from teacher.views import teacher

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("broadway/",test),
    # path("json-response",json_test),
    # path("temp",temp_render),  
    path('home/',include('home.urls')),
    path('teacher/',include('teacher.urls'))
]

