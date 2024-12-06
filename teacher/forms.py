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
        
    # label input bhanau cha jastai name, address
    # model ma bhanako attributes/data yesko aadhar ma label ra input type banai dincha  
    # class based used huncha jastai admin.py ma use gareko jastai, function based use hudaina
    # forms.ModelForm= model ma bhako sabai  data lai change garnu paryo athawa label input type ma change garnu paryo bhane lekhne models.ModelForm
    # Meta = override/ provides instructions for how django should be handle the model in database
    # override = replacing/modifying behavur of method, function or attribute in derived class
    