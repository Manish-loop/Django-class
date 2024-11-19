# api lai query set ma response chaine haine json ma chaine ho
# query ma aako response lai json ma change garna serializer ko use garne
    
from teacher.models import Teacher
from teacher.api.serializers import TeacherSerializer
from rest_framework.response import Response

def teacher_list(request):
    teacher = Teacher.objects.all() 
    serializer = TeacherSerializer(teacher, many=True)
    return Response(serializer.data)
