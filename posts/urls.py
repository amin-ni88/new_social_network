from django.urls import path

from .views import PostView, CommentView, LikeView

urlpatterns = [
    path('post/', PostView.as_view(), name='post'),
    path('post/<int:post_pk>/', PostView.as_view(), name='post'),
    path('post-list/', PostView.as_view(), name='post-list'),
    path('post/<int:post_pk>/comment/', CommentView.as_view(), name='comment'),
    path('post/<int:post_pk>/like/', LikeView.as_view(), name='like'),
]
