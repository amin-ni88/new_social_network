from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post
from .serializers import PostSerializer, CommentSerializer, LikeSerializer


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


class PostUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, post_pk):
        post = Post.objects.get(pk=post_pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDeleteView(APIView):
    def put(self, request, post_pk):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentView(APIView):
    permission_classes = [IsAuthenticated]

    def get_post(self, post_pk):
        try:
            return Post.objects.get(pk=post_pk)
        except Post.DoesNotExist:
            return False

    def get(self, request, post_pk):
        post = self.get_post(post_pk)
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # comments = Comment.objects.filter(post=post, is_approved=True)
        comments = post.comments.filter(is_approved=True)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, post_pk):
        post = self.get_post(post_pk)
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(post=post, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LikeView(APIView):
    permission_classes = [IsAuthenticated]

    def get_post(self, post_pk):
        try:
            return Post.objects.get(pk=post_pk)
        except Post.DoesNotExist:
            return False

    def get(self, request, post_pk):
        post = self.get_post(post_pk)
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)

        likes = post.likes.filter(is_liked=True).count()
        return Response({'likes': likes})

    def post(self, request, post_pk):
        post = self.get_post(post_pk)
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(post=post, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
