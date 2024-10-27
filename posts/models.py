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
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Like(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
