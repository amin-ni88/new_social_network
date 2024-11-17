from django.contrib import admin

from friendship.models import Friendship

admin.site.register(Friendship)


class FriendshipAdmin(admin.ModelAdmin):
    list_display = ('user1', 'user2', 'is_accepted', 'created_at')
    list_filter = ('user1', 'user2')
    search_fields = ('user1', 'user2')
    autocomplete_fields = ('user1', 'user2')
    actions = False

    class Meta:
        model = Friendship
        fields = '__all__'
        list_display = ('user1', 'user2')
        list_filter = ('user1', 'user2')
        search_fields = ('user1', 'user2')

    def user1(self, obj):
        return obj.user1.name

    def user2(self, obj):
        return obj.user2.name

    def is_accepted(self, obj):
        return obj.is_accepted

    def created_at(self, obj):
        return obj.created_at

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def get_readonly_fields(self, request, obj=None):
        return ['user1', 'user2']
