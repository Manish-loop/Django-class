# api lai query set ma response chaine haine json ma chaine ho
# query ma aako response lai json ma change garna serializer ko use garne
    
from teacher.models import Teacher
from teacher.api.serializers import TeacherSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail
from django.conf import settings

EMAIL_HOST_USER = settings.EMAIL_HOST_USER

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def teacher_list(request):
    teacher = Teacher.objects.all() 
    serializer = TeacherSerializer(teacher, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def teacher_first(request):
    teacher = Teacher.objects.first() 
    serializer = TeacherSerializer(teacher)
    return Response(serializer.data, status.HTTP_200_OK)

@api_view(['POST'])
def teacher_add(request):
    teacher_data = request.data
    serializer = TeacherSerializer(data=teacher_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
        # return Response({
        #     "message":"Teacher data save successfully"
        # },status.HTTP_201_CREATED)
    return Response(serializer.errors, status.HTTP_422_UNPROCESSABLE_ENTITY)

@api_view(['POST'])
def teacher_update(request,id):
    teacher = Teacher.objects.get(id=id)
    teacher_data = request.data
    serializer = TeacherSerializer(data=teacher_data, instance = teacher)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)
    return Response(serializer.errors, status.HTTP_422_UNPROCESSABLE_ENTITY)

@api_view(['POST'])
def teacher_delete(request,id):
    teacher = Teacher.objects.get(id=id)
    teacher.delete()
    return Response({
        "message":"Deleted successfully"
    },status.HTTP_204_NO_CONTENT) 
    
    
def message(request):
    send_mail(
        "Test x in Python",
        "Might be working now!",
        EMAIL_HOST_USER,
        [EMAIL_HOST_USER],
    )