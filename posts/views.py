from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post
from .serializers import PostSerializer


class PostView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, post_pk):
        try:
            post = Post.objects.get(pk=post_pk)

        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
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


class PostListView(APIView):
    def get(self, request):
        posts = Post.objects.filter(is_active=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class PostDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, post_pk):
        post = Post.objects.get(pk=post_pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)


class PostCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
