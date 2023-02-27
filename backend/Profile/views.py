from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializers import CustomUserSerializer, ProfileSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from .models import Profile




class ViewProfile(APIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        user_profile = Profile.object.get(user=user)
        serializer = self.serializer_class(user_profile)

        return Response(serializer.data, status=status.HTTP_200_OK)


