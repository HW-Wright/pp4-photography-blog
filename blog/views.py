from django.shortcuts import render
from django.views import generic
from .models import Post, Comment


# def featured_posts(request):
#     posts = Post.objects.order_by('date_created')[:3]
#     context = {
#         'posts' : posts
#     }
#     template = 'inex.html'
#     return render(request, template, context)


class FeaturedPosts(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=True).order_by('-date_created')[:3]
    template_name = 'index.html'