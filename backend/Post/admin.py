from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('unique_id','user','created_at')
    search_fields = ('user','likes')
    list_filter = ('user','created_at',)

    ordering = ('likes','created_at')

admin.site.register(Post, PostAdmin)
