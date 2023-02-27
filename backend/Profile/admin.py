from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('email','phone_number','location','created_at')
    search_fields = ('email','phone_number')
    list_filter = ('email','phone_number','sex','location','created_at')

    ordering = ('email','phone_number')


admin.site.register(Profile, ProfileAdmin)
