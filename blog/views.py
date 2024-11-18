from django.shortcuts import render
from django.utils import timezone
from django.views import View

from social_media.models import SocialMedia
from .models import Post


# Create your views here.

class IndexView(View):
    def get(self, request):
        special_posts = Post.objects.filter(is_special=True, released_at__lte=timezone.now()).order_by('-created_at')
        last_post = Post.objects.filter(is_special=False, released_at__lte=timezone.now()).order_by(
            '-created_at').first()
        top_8_posts = Post.objects.filter(is_special=False, released_at__lte=timezone.now()).order_by('-created_at')[
                      1:9]
        urgent_post = Post.objects.filter(is_urgent=True, released_at__lte=timezone.now()).order_by(
            '-created_at').first()
        social_media_info = SocialMedia.objects.first()

        context = {
            'special_posts': special_posts,
            'last_post': last_post,
            'top_8_posts': top_8_posts,
            'urgent_post': urgent_post,
            'social_media_info': social_media_info
        }

        return render(request, 'blog/index.html', context)


class PostDetailView(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            'post': post
        }

        return render(request, 'blog/post_detail.html', context)
