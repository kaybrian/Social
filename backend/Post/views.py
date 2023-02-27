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

class PostDetailView(APIView):
    serializer_class = PostsSerilizer
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser,)

    def get(self, request, pk):
        post = get_object_or_404(Post, unique_id=pk)
        serializer = self.serializer_class(post, many=False)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        user = request.user
        post = get_object_or_404(Post, unique_id=pk)

        if post.user == user:
            try:
                serializer = PostSerializer(
                    post, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Post.DoesNotExist:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"Message":"Sorry you are not allowed to do this"}, status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, pk):
        user = request.user
        post = get_object_or_404(Post, unique_id=pk)

        if post.user == user:
            try:
               post.delete()
               return Response({"Message":"Post was deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)
            except Post.DoesNotExist:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"Message":"Sorry you are not allowed to do this"}, status=status.HTTP_401_UNAUTHORIZED)


