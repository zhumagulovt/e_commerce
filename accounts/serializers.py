from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, data):

        username = data.get('username')
        password = data.get('password')
        request = self.context.get('request')

        if username and password:
            user = authenticate(username=username, password=password, request=request)

            if not User:
                raise serializers.ValidationError("Incorrect username or password")
        else:
            raise serializers.ValidationError("username and password are required")

        data['user'] = user
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class PasswordChangeSerializer(serializers.Serializer):
    model = User

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
