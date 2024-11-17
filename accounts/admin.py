from django.contrib import admin
from .models import User
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','first_name', 'last_name', 'email', 'is_superuser', 'is_active']
    list_filter = ['is_superuser', 'is_active']
    search_fields = ['first_name', 'last_name', 'email']
    date_hierarchy = 'date_joined'

    ordering = ['first_name', 'last_name']
    fieldsets = (
        ('اطلاعات کاربر', {
            'fields': ('first_name', 'last_name', 'email', 'is_superuser', 'is_active')
        }),

    )
    readonly_fields = ['date_joined']
    filter_horizontal = ['groups', 'user_permissions']
    list_per_page = 10
    actions_on_top = True
    actions_on_bottom = True
    save_on_top = True
    save_on_bottom = True
    list_select_related = True

