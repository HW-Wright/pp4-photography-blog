import re
from django.db.models import Count
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Comment
from .forms import CommentForm, PostForm, EditForm



class FeaturedPosts(generic.ListView):
    model = Post
    liked_posts = Post.objects.annotate(likes_count=Count('likes'))
    queryset = liked_posts.order_by('-likes_count')[:3]
    template_name = 'index.html'



class SpecificPost(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=True)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.photo_comment.order_by("date_created")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request, 
            'specific_post.html',
            {
                'post': post,
                'comments': comments,
                'liked': liked,
                'comment_form': CommentForm()
            },
        )

    @method_decorator(login_required)
    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=True)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.photo_comment.order_by("date_created")
        liked = False

        if not request.user.is_authenticated:
            raise Http404

        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.created_by = request.user
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return redirect('specific_post', slug=slug)



class LikePost(LoginRequiredMixin, View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('specific_post', args=[slug]))


class AllPosts(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=True).order_by('-date_created')
    template_name = 'blog.html'


@login_required
def edit_post(request, slug):
    queryset = Post.objects.filter(status=True)
    post = get_object_or_404(queryset, slug=slug)

    if request.method == 'POST':
        form = EditForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('specific_post', slug=slug)
    else:
        form = EditForm(instance=post)
    
    context = {
        'form': form
    }

    return render(request, 'edit_post.html', context)


@login_required
def add_post(request):
    form = PostForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.created_by = request.user
            new_slug = new_post.title.lower()
            new_slug2 = re.sub(r'[^\w]', ' ', new_slug)
            new_post.slug = new_slug2.replace(" ", "-")
            new_post = form.save()
            return redirect('homepage')
        else:
            form = PostForm(request.POST, request.FILES)
    
    context = {
        'form': form
    }

    return render(request, 'add_post.html', context)


@login_required
def delete_post(request, slug):
    queryset = Post.objects.filter(status=True)
    post = get_object_or_404(queryset, slug=slug)
    if request.user == Post.created_by:
        print('deleted')
        post.delete()
    else:
        print('notdeleted')

    return redirect('blog')


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == Comment.created_by:
        print('deleted')
        comment.delete()
    else:
        print('notdeleted')

    return redirect('blog')



