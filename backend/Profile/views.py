from django.shortcuts import render, get_object_or_404
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializers import CustomUserSerializer, ProfileSerializer, UpdateProfile
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from .models import Profile
from rest_framework.parsers import MultiPartParser


class ViewProfile(APIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser,)

    def get(self, request):
        user = request.user
        user_profile = Profile.objects.get(user=user)
        serializer = self.serializer_class(user_profile)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        try:
            profile = Profile.objects.get(user=request.user)
            serializer = UpdateProfile(
                profile, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        except Profile.DoesNotExist:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)



class ViewAnotherProfile(APIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        person = get_object_or_404(Profile, pk=pk)
        serializer = self.serializer_class(person)
        return Response(serializer.data, status=status.HTTP_200_OK)

