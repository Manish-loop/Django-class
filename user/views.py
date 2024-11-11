from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from user.forms import LoginForm, RegisterForm
# Create your views here.


def user_login(request):
    if request.user.is_authenticated:
        return redirect('/home')
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username') # username chaina bhane none pathaucha
            password = request.POST.get('password') # dictionary ko get
            user = authenticate(username=username, password=password) # authenticate le raw password lai change garcha hashing ma
            if user is not None:
                login(request, user)
            return redirect('/home')
    context = {
        "form":form
    }
    return render(request, 'user/login.html', context)

def user_register(request):
    form = RegisterForm()
    if request.method== "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) # commit=False le hold garaucha certain kaam garna ko lagi
            user.set_password(request.POST['password']) # Set password le encrypt garcha request.POST['password'] lai
            user.save() 
            return redirect('/home')
    context = {
        "form":form
    }
    return render(request, 'user/register.html', context)