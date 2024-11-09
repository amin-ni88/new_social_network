from rest_framework import serializers

from .models import Post, Like, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('user', 'title', 'content', 'is_active', 'caption', 'is_public')
        extra_kwargs = {
            'user': {'read_only': True},
            
        }


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('post', 'user', 'text')
        extra_kwargs = {
            'post': {'read_only': True},
            'user': {'read_only': True}
        }
        
class CommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fieldes = ('user', 'post')
        extra_kwargs = {
            'user': {'read_only': True},
            'post': {'read_only': True},
            'is_liked': {'required': False}
        }
        
        
class CommentReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('post', 'user', 'text')
        extra_kwargs = {
            'post': {'read_only': True},
            'user': {'read_only': True},
        }


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('post', 'user', 'is_liked')
        extra_kwargs = {
            'post': {'read_only': True},
            'user': {'read_only': True},
            'is_liked': {'required': False}
        }
