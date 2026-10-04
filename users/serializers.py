from django.contrib.auth import get_user_model
from .models import CustomUser
from rest_framework import serializers


User=get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","username","bio","avatar","date_joined"]   
        read_only_fields=["id","date_joined"]


class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True,min_length=8)
    password2=serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields=["username","email","password","password2"]

    def validate(self,attrs):
        if attrs["password"]!=attrs["password2"]:
            raise serializers.ValidationError({"error":"password doesn't match"})
        return attrs

    def create(self,validated_data):
        validated_data.pop("password2")
        return User.objects.create_user(**validated_data)

