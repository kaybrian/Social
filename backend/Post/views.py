from django.shortcuts import render
from .serializers import PostsSerilizer,PostSerializer
from django.shortcuts import render, get_object_or_404
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from .models import Post
from rest_framework.parsers import MultiPartParser



class PostsView(APIView):
    serializer_class = PostsSerilizer
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser,)


    def get(self, request):
        posts = Post.objects.all()
        serializer = self.serializer_class(posts, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        user = request.user
        serializer = PostSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_200_OK)


# class CreatePosts(APIView):
#     serializer_class = PostSerializer
#     permission_classes = [IsAuthenticated]
#     parser_classes = (MultiPartParser,)

#     def get(self, request):
#         posts = Post.objects.all()
#         serializer = self.serializer_class(posts, many=True)


#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         user = request.user
#         serializer = PostSerializer(data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save(user=user)
#             return Response(serializer.data, status=status.HTTP_200_OK)


