from django import forms
from teacher.models import Teacher,SchoolClass

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        # exclude = ['name']
        
        
class ClassForm(forms.ModelForm):
    class Meta:
        model = SchoolClass
        fields= '__all__'