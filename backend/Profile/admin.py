from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('email','phone_number','location')
    search_fields = ('email','phone_number')


admin.site.register(Profile, ProfileAdmin)
