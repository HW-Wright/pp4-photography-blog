from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post, Comment


class FeaturedPosts(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=True).order_by('-date_created')[:3]
    template_name = 'index.html'

class SpecificPost(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=True)
        post = get_object_or_404(queryset, slug=slug)
        comments = Comment.objects.order_by('-date_created')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request, 
            'specific_post.html',
            {
                'post': post,
                'comments': comments,
                'liked': liked
            },
        )

class AllPosts(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=True).order_by('-date_created')
    template_name = 'blog.html'