from django import forms
from django.contrib.auth.models import User 

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)  
    
    
class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)  
    
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
        ]