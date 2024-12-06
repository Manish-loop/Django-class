from django import forms
from django.contrib.auth.models import User 

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)  

# widget le kasto type ko banauna khoji racha bhanne kura define garcha
# password CharField ma save bhaye pani PasswordInput ma hunu paryo
# aru pani options cha widget ko lagi forms.TextInput, forms.NumberInput, forms.BooleanInput, etc.

# Form lai validate garne ho, yesma save garne hoina tai vayera models chaidaena 
# validate matra garne vayeko le form ma garne ho model chaidaena


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
        
class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput)
    new_password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    