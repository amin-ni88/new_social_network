from django.urls import path

from .views import (UserListView, RequestView,
                    RequsetListView, AcceptView,
                    RejectView, FriendListView)

urlpatterns = [
    path('users_list/', UserListView.as_view(), name='user-list'),
    path('request/', RequestView.as_view(), name='request'),
    path('request_list', RequsetListView.as_view(), name='request-list'),
    path('accept/', AcceptView.as_view(), name='accept'),
    path('reject/', RejectView.as_view(), name='reject'),
    path('friends/', FriendListView.as_view(), name='friends'),

]
