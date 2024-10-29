from django.urls import path

from .views import PostView

urlpatterns = [
    path('post/', PostView.as_view(), name='post'),
    path('post/<int:post_pk>/', PostView.as_view(), name='post'),
    path('post-list/', PostView.as_view(), name='post-list'),
]
