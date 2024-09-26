from django.shortcuts import render
from teacher.models import Teacher
# Create your views here.

def teacher(request):
    data = Teacher.objects.filter(is_active=True)
    data_dict = {
        "teacher": data
    }
    return render