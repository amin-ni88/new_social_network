from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Friendship
from .serializers import UserListSerializer

User = get_user_model()


class UserListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = User.objects.filter(is_active=True,
                                    is_verified=True,
                                    is_superuser=False,
                                    is_staff=False)
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data)


class RequestView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_id = request.data.get('user')

        try:
            user = User.objects.get(pk=user_id)
            serializer = UserListSerializer(user)
        except User.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        Friendship.objects.get_or_create(user_id=user.id, friend=request.user.id)

        return Response({'detail': 'Request sent'}, status=status.HTTP_201_CREATED)

    def delete(self, request):
        user_id = request.data.get('user')

        try:
            user = User.objects.get(pk=user_id)
            Friendship.objects.get_or_create(user_id=user.id, friend=request.user.id)
            return Response({'detail': 'Request deleted'}, status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response({'detail': 'Request deleted'}, status=status.HTTP_201_CREATED)


class RequsetListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_id = request.data.get('user')
        friendship = Friendship.objects.filter(request_to=request.user, friend=request.user.id, is_active=False)
        users = [fr.request_from for fr in friendship]
        serializer = UserListSerializer(friendship, many=True)
        return Response(serializer.data)


class RequsetDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        user_id = request.data.get('user')


class AcceptView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_id = request.data.get('user')

        try:
            user = User.objects.get(pk=user_id)
            Friendship.objects.get(request_from=user, request_to=request.user, is_accepted=False)
            return Response({'detail': 'Request deleted'}, status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        friendship.is_accepted = True
        friendship.request_from = request.user
        friendship.request_to = request.user
        friendship.save()

        return Response({'detail': 'Request accepted'}, status=status.HTTP_201_CREATED)


class RejectView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_id = request.data.get('user')
        request_from = request.data.get('request_from')
        request_to = request.data.get('request_to')
        return Response({'detail': 'Request rejected'}, status=status.HTTP_201_CREATED)


class FriendListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_id = request.data.get('user')
        friendship = Friendship.objects.filter(
            Q(request_from=request.user.id, request_to=request.user.id) | Q(id=request.user.id),
            is_accepted=True,
            is_active=True
        )

        users = [fr.request_from for fr in friendship]
        serializer = UserListSerializer(friendship, many=True)
        return Response(serializer.data)
