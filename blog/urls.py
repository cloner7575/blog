from django.urls import path, re_path

from .views import IndexView, PostDetailView, AllPostsView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    re_path(r'^(?P<slug>[\w-]+)/$', PostDetailView.as_view(), name='post_detail'),
    path('posts/', AllPostsView.as_view(), name='all_posts'),
]
