from rest_framework.views import APIView
from teacher.models import Teacher, SchoolClass
from teacher.api.serializers import TeacherSerializer, SchoolClassSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle

# Vuew = custom kaam haru so yo use gardainau
# APIView = custom kaam + extra aru kaam haru
# GenericView = APIView ko kaam + extra 

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
        pass
        # teacher = Teacher.objects.all() 
        # serializer = TeacherSerializer(teacher, many=True)
        # return Response(serializer.data)
    
    def delete(id):
        pass
    
class SchoolClassView(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]
    
    def get(self,request):
        data = SchoolClass.objects.all()
        serializer = SchoolClassSerializer(data, many=True)
        return Response(serializer.data, status.HTTP_200_OK)