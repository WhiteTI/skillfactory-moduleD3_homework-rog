import datetime

from django.views.generic import ListView, DeleteView
from .models import Post, Category, Author


class PostList(ListView):
    model = Post
    template_name = 'news/posts.html'
    context_object_name = 'posts'


class PostDetail(DeleteView):
    model = Post
    template_name = 'news/post.html'
    context_object_name = 'post'