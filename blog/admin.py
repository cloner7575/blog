from django.contrib import admin
from django.utils.safestring import mark_safe

from .forms import PostAdminForm
from .models import Post, Category, Tag, Author


# Register your models here.




@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ['title', 'category', 'author', 'is_special', 'is_published', 'created_at']
    list_filter = ['category', 'author', 'is_special', 'is_published']
    search_fields = ['title', 'content']
    date_hierarchy = 'created_at'
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'color_tag']

    # show color as a square
    def color_tag(self, obj):
        return mark_safe(f'<div style="width: 50px; height: 50px; background-color: {obj.color};"></div>')

    color_tag.short_description = 'رنگ'


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['user', ]
