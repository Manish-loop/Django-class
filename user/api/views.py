from django.contrib.auth.models import User
from user.api.serializers import UserSerializer, LoginSerializer  #, RegisterSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from user.api.services import UserServices
from ipware import get_client_ip

@api_view(['GET'])
def user_info(request):
    user = User.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def user_login(request):
    data = request.data
    serializer = LoginSerializer(data=data)
    if serializer.is_valid():
        username = request.data['username' ]
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            serializer_data = UserSerializer(user)
            UserServices.create_user_activity(
                request,
                user = user,
                ip_address = get_client_ip(request)[0],
                modules = "Login",
                user_agent = request.META.get('HTTP_USER_AGENT',None)
                )
            
            return Response(serializer_data.data)
        return Response({
            "error":"Password does not match"
        })
    return Response(serializer.errors, status.HTTP_422_UNPROCESSABLE_ENTITY)


# # register api
# @api_view(['POST'])
# def user_register(request):
#         serializer = RegisterSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             return Response(
#                 {"message": "User registered successfully!", "user": serializer.data},
#                 status=status.HTTP_201_CREATED
#             )