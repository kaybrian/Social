from rest_framework import serializers
from .models import Post,Comment
from users.models import CustomUser




class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'name', 'date_of_birth')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('image','image_url','description')

    def to_representation(self, instance):
            representation = super().to_representation(instance)
            representation.pop("image")
            return representation

class AddCommentToPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('unique_id','comment',)

class AddCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('unique_id','user','post','comment','likes','created_on')

class PostsSerilizer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    image_url = serializers.ReadOnlyField()
    class Meta:
        model = Post
        fields = ('unique_id','user','image','image_url','description','number_of_likes','created_at')

    def to_representation(self, instance):
            representation = super().to_representation(instance)
            representation.pop("image")
            return representation


# adding comments to the posts

