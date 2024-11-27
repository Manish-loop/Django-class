from django.contrib.auth.models import User
from user.api.serializers import UserSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth import  authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from user.api.services import UserServices
from ipware import get_client_ip

from django.core.mail import send_mail
from django.template.loader import render_to_string

from django.conf import settings
from django.utils.html import strip_tags


host_mail = settings.EMAIL_HOST_USER


@api_view(['GET'])
def user_info(request):
    user = User.objects.all()
    serialzier = UserSerializer(user, many=True)
    return Response(serialzier.data)


@api_view(['POST'])
def user_login(request):
    data = request.data + 0
    serializer = LoginSerializer(data=data)
    if serializer.is_valid():
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            serializer_data = UserSerializer(user)
            UserServices.create_user_actvitiy(
                request,
                user=user,
                ip_address = get_client_ip(request)[0],
                modules = "Login",
                user_agent = request.META.get('HTTP_USER_AGENT', None)
            )
            f'Yoh have been logged in from {request.META.get("HTTP_USER_AGENT")}  and ip is {get_client_ip(request)[0]}',

            if user.email:
                send_mail(
                    "Login",
                    strip_tags(render_to_string('user/email.html', context={
                        'user_agent':request.META.get("HTTP_USER_AGENT"),
                        'ip_address':get_client_ip(request)[0]
                    })),
                    host_mail,
                    [user.email]
                )


            return Response(serializer_data.data)
        return Response({
            "error":"Password does not match"
        })
    return Response(serializer.errors, status.HTTP_422_UNPROCESSABLE_ENTITY)


# try register api 

























# from django.contrib.auth.models import User
# from user.api.serializers import UserSerializer, LoginSerializer  #, RegisterSerializer
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import status
# from django.contrib.auth import authenticate
# from rest_framework_simplejwt.tokens import RefreshToken
# from user.api.services import UserServices
# from ipware import get_client_ip

# from django.core.mail import send_mail
# from django.template.loader import render_to_string

# from django.conf import settings
# from django.utils.html import strip_tags

# host_mail = settings.EMAIL_HOST_USER

# @api_view(['GET'])
# def user_info(request):
#     user = User.objects.all()
#     serializer = UserSerializer(user, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def user_login(request):
#     data = request.data
#     serializer = LoginSerializer(data=data)
#     if serializer.is_valid():
#         username = request.data['username' ]
#         password = request.data['password']
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             serializer_data = UserSerializer(user)
#             UserServices.create_user_activity(
#                 request,
#                 user = user,
#                 ip_address = get_client_ip(request)[0],
#                 modules = "Login",
#                 user_agent = request.META.get('HTTP_USER_AGENT',None)
#                 )
#             f'Yoh have been logged in from {request.META.get("HTTP_USER_AGENT")}  and ip is {get_client_ip(request)[0]}',
                
#             if user.email:
#                 send_mail(
#                     "Login",
#                     strip_tags(render_to_string('user/email.html', context={
#                         'user_agent':request.META.get("HTTP_USER_AGENT"),
#                         'ip_address':get_client_ip(request)[0]
#                     })),
#                     host_mail
#                     [user.mail]
#                 )
                
#             return Response(serializer_data.data)
#         return Response({
#             "error":"Password does not match"
#         })
#     return Response(serializer.errors, status.HTTP_422_UNPROCESSABLE_ENTITY)


# # # register api
# # @api_view(['POST'])
# # def user_register(request):
# #         serializer = RegisterSerializer(data=request.data)
# #         if serializer.is_valid():
# #             user = serializer.save()
# #             return Response(
# #                 {"message": "User registered successfully!", "user": serializer.data},
# #                 status=status.HTTP_201_CREATED
# #             )