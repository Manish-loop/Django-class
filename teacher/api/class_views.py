import django_filters
from rest_framework.views import APIView
from teacher.models import Teacher, SchoolClass
from teacher.api.serializers import TeacherSerializer, SchoolClassSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from rest_framework.generics import GenericAPIView
from .filter_set import SchoolFilters

# View = custom kaam haru so yo use gardainau
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
    
# class SchoolClassView(APIView):
#     permission_classes = [IsAuthenticated]
#     throttle_classes = [UserRateThrottle]
    
#     def get(self,request):
#         data = SchoolClass.objects.all()
#         serializer = SchoolClassSerializer(data, many=True)
#         return Response(serializer.data, status.HTTP_200_OK)
    
    
class SchoolClassView(GenericAPIView):
    # permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]
    serializer_class = SchoolClassSerializer
    queryset = SchoolClass.objects.all()
    filterset_fields = ['is_active']
    
    def get(self,request):
        data = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(data, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    
    
class SerchClassView(GenericAPIView):
    queryset = SchoolClass.objects.all()
    serializer_class = SchoolClassSerializer
    throttle_classes = [UserRateThrottle]

    def get(self, request):
        print(request.GET)
        data = self.get_queryset()
        if request.GET.get('search'):
            data = SchoolClass.objects.filter(name__icontains=request.GET.get('search'))
        serializer = self.get_serializer(data, many=True)
        return Response(serializer.data, status.HTTP_200_OK)