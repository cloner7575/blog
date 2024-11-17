from django.shortcuts import render
from django.views import View
from .models import Post

# Create your views here.

class IndexView(View):
    def get(self, request):
        special_posts = Post.objects.filter(is_special=True)
        last_post = Post.objects.filter(is_special=False).order_by('-created_at').first()
        top_8_posts = Post.objects.filter(is_special=False).order_by('-created_at')[1:9]
        context = {
            'special_posts': special_posts,
            'last_post': last_post,
            'top_8_posts': top_8_posts
        }

        return render(request, 'blog/index.html', context)


class PostDetailView(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            'post': post
        }

        return render(request, 'blog/post_detail.html', context)
