from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    caption = models.TextField(max_length=2048)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    is_public = models.BooleanField(default=False)
    location = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name: str = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title


class PostFile(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    file = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name: str = 'Post File'
        verbose_name_plural = 'Post Files'


class Comment(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.PROTECT, related_name='comments')
    # parent = models.ForeignKey(to='self', null=True, blank=True, on_delete=models.PROTECT, related_name='children')
    text = models.TextField()
    likes = models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='likes')
    is_approved = models.BooleanField(default=False)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name: str = 'Comment'
        verbose_name_plural = 'Comments'
        unique_together = (('user', 'post'),)
        ordering = ['created_at']

class CommentReply(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name: str = 'Comment Reply'
        verbose_name_plural = 'Comment Replies'
        unique_together = (('user', 'comment'),)
        ordering = ['created_at']

class CommentLike(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name: str = 'Comment Like'
        verbose_name_plural = 'Comment Likes'
        unique_together = (('user', 'comment'),)
        ordering = ['created_at']




class Like(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.PROTECT, related_name='likes')
    is_liked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name: str = 'Like'
        verbose_name_plural = 'Likes'
        unique_together = (('user', 'post'),)
