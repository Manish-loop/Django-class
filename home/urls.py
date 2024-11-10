from django.urls import path
from home.views import *


urlpatterns = [
    path('',home_render),
    path('broadway',test),
    path('json-response',json_test),
    path('temp',temp_render),
]