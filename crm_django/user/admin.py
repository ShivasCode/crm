from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user.models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email','is_staff', 'is_active',)
    list_filter = ('email','is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email','first_name','last_name','password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','password1','first_name',"last_name",'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)