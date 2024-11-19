# json => dict
# object => js , in js json is called object
# dict => python , dict in python for json 
# Meta is used to overwrite class Here in below it overwrites TeacherSerializer

from rest_framework import serializers
from teacher.models import Teacher

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
        # fields = [
        #     'id',
        #     'name'
        # ]