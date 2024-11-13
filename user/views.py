from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from user.forms import LoginForm, RegisterForm, ChangePasswordForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
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

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

@login_required()

def change_password(request):
    form = ChangePasswordForm()
    if request.method == "POST":
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            old_password = request.POST('old_password')
            new_password = request.POST('new_password')
            confirm_password = request.POST('confirm_password')
            user = request.user
            if not user.check_password(old_password):
                return HttpResponse("old password does not match")
            
            elif new_password != confirm_password:
                return HttpResponse("new password do not match")
            
            #compare old password and new password should not match
            user.set_password(new_password)
            user.save() 
            return redirect('/home')

    context = {
        "form": form
    }
    return render(request, 'user/change_password.html', context)