from django.contrib import admin
from .models import Post,Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('unique_id','user','created_at')
    search_fields = ('user','likes')
    list_filter = ('user','created_at',)

    ordering = ('likes','created_at')

admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('unique_id','post','user','created_on')
    search_fields = ('user','likes','post')
    list_filter = ('post','user','created_on',)
    ordering = ('likes','created_on')

admin.site.register(Comment, CommentAdmin)
