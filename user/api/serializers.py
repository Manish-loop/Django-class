from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken


class TokenSerializer(serializers.Serializer):
    refresh= serializers.CharField()
    access= serializers.CharField()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = [
            'password',
            'groups',
        ]
        # fields = [
        #     'id',
        #     'username',
        #     'token'
        # ]
        # fields = '__all__'
    
    def to_representation(self, instance):
        token = RefreshToken.for_user(instance)
        data = super().to_representation(instance)
        data['refresh']=str(token)
        data['access']=str(token.access_token)
        return data
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    password = serializers.CharField(required=True, allow_null=False, allow_blank=False)

    def validate(self, validated_data):
        return validated_data

    def validate_username(self, username):
        if len(username)<3:
            raise ValidationError("Username lens must be more than 3") 
        return username
    
    def validate_password(self,password):
        return password
    
# class RegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

#     class Meta:
#         model = User
#         fields = ['username', 'password']

#     def validate(self, data):
#         username = data.get('username')
#         password = data.get('password')

#         # Check if username and password are the same
#         if username and password and username == password:
#             raise serializers.ValidationError(
#                 {"password": "Password cannot be the same as the username."}
#             )

#         return data
