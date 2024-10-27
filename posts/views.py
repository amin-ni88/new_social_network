from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post
from .serializers import PostSerializer


class PostView(APIView):
    def get(self, request):
        posts = Post.objects.all()

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        post = Post.objects.get(pk=request.data['id'])
        post.title = request.data['title']
        post.body = request.data['body']
        post.save()
        return Response('Post successfully saved', status=status.HTTP_201_CREATED)

    def delete(self, request):
        post = Post.objects.get(pk=request.data['id'])
        post.delete()

    def patch(self, request):
        post = Post.objects.get(pk=request.data['id'])
        post.title = request.data['title']
        post.body = request.data['body']
        post.save()

    def head(self, request):
        posts = Post.objects.all()
        for post in posts:
            post.title = post.title
            post.body = post.body
            post.save()

    def options(self, request):
        posts = Post.objects.all()
        posts = posts.filter(title__icontains=request.data['title'])
        for post in posts:
            post.title = post.title
            post.body = post.body
            post.save()
