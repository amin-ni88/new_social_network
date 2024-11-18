from django.urls import path

from .views import UserListView

urlpatterns = [
    path('users_list/', UserListView.as_view(), name='user-list'),
    path('request/', ),
    path('request_list'),
    path('accept/'),
    path('reject/'),
    path('friends/'),

]
