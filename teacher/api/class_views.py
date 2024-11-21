from rest_framework.views import APIView
from teacher.models import Teacher
from teacher.api.serializers import TeacherSerializer
from rest_framework.response import Response
from rest_framework import status


class TeacherView(APIView):

    def get(self, request):
        teacher = Teacher.objects.all()
        serializer = TeacherSerializer(teacher, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        teacher_data = request.data
        serializer = TeacherSerializer(data=teacher_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
            # return Response({
            #     "message":"Teacher data save successfully"
            # }, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_422_UNPROCESSABLE_ENTITY)
    

class TeacherUpdateAndDelete(APIView):
    def put(id):
        teacher = Teacher.objects.all() 
        serializer = TeacherSerializer(teacher, many=True)
        return Response(serializer.data)
    
    def delete(id):
        pass
    
class SchoolClassView(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]
    
    def get(self,request):
        data = SchoolClass.objects.all()
        serializer = SchoolClassSerializer(data, many=True)
        return Response(serializer)