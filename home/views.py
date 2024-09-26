from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from home.models import Home
# Create your views here.
def test(request):
    return HttpResponse("<h1>Hello django</h1>")
    
    
    #  return HttpResponse(       This is in string cannot provide in json form ss
    #     f'{"name:""this is test"}'
    # )



def json_test(request):
    return JsonResponse({
        "name": "This is django test"
    }) 
    
def temp_render(request):
    desc = f'this is from views and today date and time is {datetime.now()}'
    data = {
        "test":desc
    }
    return render(request, 'home/index.html',data)


def home_render(request):
    qs = Home.objects.all()
    data = {
        "home":qs
    }
    return render(request, 'home/home_models.html',data)
    