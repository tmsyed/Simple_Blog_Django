from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'text', 'created_date')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
