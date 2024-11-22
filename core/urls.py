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
# from home.views import test, json_test,temp_render ,home_render # home folder ko views.py file ko test function lai import garne 
# from teacher.views import teacher
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls), 
    path('home/',include('home.urls')),
    path('teacher/',include('teacher.urls')),
    path('user/',include('user.urls')),
    
]


# apiurls=[
#     path('api/teacher', include('teacher.api.urls'))
# ]

apiurls=[
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  
    path('api/user/', include('user.api.urls')), 
    path('api/teacher/', include('teacher.api.urls')),
    
    
    ## classbased view
    path('api/teacher_class/', include('teacher.api.class_base_urls'))
]


urlpatterns= urlpatterns+apiurls
# urlpatterns.extend(apiurls) another option
