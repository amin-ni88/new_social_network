from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('date_joined', 'last_login')
        write_only_fields = ('date_joined', 'last_login')
        depth = 1
        depth_first = True
        depth_limit = None
        depth_order = None
