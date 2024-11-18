from django.contrib import admin
from .models import SocialMedia
# Register your models here.

@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ['telegram_channel', 'telegram_member', 'instagram_page', 'instagram_follower']
    list_display_links = ['telegram_channel', 'instagram_page']
    list_editable = ['telegram_member', 'instagram_follower']

