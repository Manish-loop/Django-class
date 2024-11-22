# json => dict
# object => js , in js json is called object
# dict => python , dict in python for json 
# Meta is used to overwrite class Here in below it overwrites TeacherSerializer

from rest_framework import serializers
from teacher.models import Teacher, SchoolClass

class TeacherSerializer(serializers.ModelSerializer):
    # name = serializers.IntegerField()
    class Meta:
        model = Teacher
        fields = '__all__'
        # fields = [
        #     'id',
        #     'name'
        # ]
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['class']="python django"
        data['name_id']=data['name'] + str(data['id'])
        data.pop('salary')
        data['teacher_email'] = data.pop('email')
        return data
    
    # def to_representation(self, instance):
    #     return {
    #         "name":instance.name,
    #         "teacher":instance.email
    #     }    
    #  This should process should not be used 
    
class SchoolClassSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(many=True)
    class Meta:
        model = SchoolClass
        fields = "__all__"