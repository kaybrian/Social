from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group




class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    list_display = ('name','email', 'date_of_birth')
    list_filter = ('email','date_of_birth',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('date_of_birth',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'date_of_birth', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(CustomUser, UserAdmin)
admin.site.unregister(Group)

