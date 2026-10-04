from .serializers import UserSerializer, RegisterSerializer
from rest_framework import generics,status
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny,IsAuthenticatedOrReadOnly,IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response


User=get_user_model

class RegisterView(generics.CreateAPIView):
    serializer_class=RegisterSerializer
    permission_classes=[AllowAny]


class MeView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        return Response(UserSerializer(request.user).data)

    def patch(self,request):
        serializer=UserSerializer(request.user, request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    