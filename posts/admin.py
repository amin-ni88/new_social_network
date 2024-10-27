from django.contrib import admin

from .models import Post, PostFile


class PostFileInlineAdmin(admin.StackedInline):
    model = PostFile
    fields = ('file', 'title', 'author')
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'content')
    list_filter = ('author', 'date')
    date_hierarchy = 'date'
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [PostFileInlineAdmin]

    def has_add_permission(self, request):
        return False

# @admin.register(PostFile)
# class PostFileAdmin(admin.ModelAdmin):
#     list_display = ('title','author','date','content')
#     list_filter = ('author','date')
#     date_hierarchy = 'date'
#     search_fields = ['title']
#     prepopulated_fields = {'slug': ('title',)}
#     def has_add_permission(self, request):
#         return False
