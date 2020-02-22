import crypt
from rest_framework import serializers
from rest_framework_mongoengine.serializers import DocumentSerializer
from app_chat.models import User
from mongoengine import StringField
from app_chat.constants import CONST_USERNAME_LENGTH, CONST_PASSD_LENGTH

class UserSerializer(DocumentSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        encrypt_password = crypt.crypt(password)
        validated_data['password'] = encrypt_password
        validated_data['name'] = validated_data['first_name']+' '+validated_data['last_name']
        user = User(**validated_data)
        user.save()
        return user


class UserReadSerializer(DocumentSerializer):
    class Meta:
        model = User
        fields = ['id', 'created_at', 'first_name', 'last_name', 'name', 'username']


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=CONST_USERNAME_LENGTH)
    password = serializers.CharField(max_length=CONST_PASSD_LENGTH)
