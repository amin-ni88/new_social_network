from django.contrib.auth import get_user_model
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

    def get(self, request):
        user_id = request.data.get('user')

        try:
            user = User.objects.get(pk=user_id)
            serializer = UserListSerializer(user)
        except User.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        Friendship.objects.create(user_id=user.id, friend=request.user.id)
        return Response({'detail': 'Request sent'}, status=status.HTTP_201_CREATED)
