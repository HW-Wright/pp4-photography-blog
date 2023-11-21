from django.shortcuts import render
from django.views import generic
from .models import Post, Comment

class FeaturedPosts(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=True).order_by('-date_created')
    template_name = 'index.html'
    paginate_by = 9