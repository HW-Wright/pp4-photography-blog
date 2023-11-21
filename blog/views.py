from django.shortcuts import render
from django.views import generic
from .models import Post, Comment


# def featured_posts(request):
#     posts = Post.objects.all()
#     context = {
#         'posts' : posts
#     }
#     return render(request, '/templates/index.html/', context)


class FeaturedPosts(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=True).order_by('-date_created')
    template_name = 'index.html'
    paginate_by = 9