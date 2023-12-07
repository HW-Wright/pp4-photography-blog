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
from .models import Post, Comment, Editor, UserProfile
from .forms import CommentForm, PostForm, EditForm, DeleteForm


"""This view will render the three most like posts in index.html"""

class FeaturedPosts(generic.ListView):
    model = Post
    liked_posts = Post.objects.annotate(likes_count=Count('likes'))
    queryset = liked_posts.order_by('-likes_count')[:3]
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['editors'] = Editor.objects.all()

        return context


"""This view will render the desired post and all it's
    comments to Specific_post.html.
    The second function handles posting of comments"""

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


"""This view will amend the amounts of likes on a post when used"""

class LikePost(LoginRequiredMixin, View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('specific_post', args=[slug]))


"""This view will render all Post objects in blog.html"""

class AllPosts(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=True).order_by('-date_created')
    template_name = 'blog.html'


"""This view ensures users are validated and renders the EditForm"""

@login_required
def edit_post(request, slug):
    queryset = Post.objects.filter(status=True)
    post = get_object_or_404(queryset, slug=slug, created_by=request.user)

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


"""This view will render the PostForm in add_post.html"""

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


"""This view will render the DeletePost form in delete_post.html"""

@login_required
def delete_post(request, slug):
    queryset = Post.objects.filter(status=True)
    post = get_object_or_404(queryset, slug=slug, created_by=request.user)

    if request.method == 'POST':
        form = DeleteForm(request.POST, instance=post)
        if form.is_valid():
            post.delete()
            return redirect('blog')
    else:
        form = DeleteForm(instance=post)
    context = {
        'form': form
    }

    return render(request, 'delete_post.html', context)


"""Thsi view will remove the resired comment from the specific_post"""

@login_required
def delete_comment(request, comment_id, slug):
    comment = get_object_or_404(
        Comment, id=comment_id, created_by=request.user)
    if request.user == comment.created_by:
        comment.delete()

    return redirect('specific_post', slug=slug)


"""All views beloe are to render custom error pages in the browser"""

def handle404(request, exeption):
    return render(request, '404.html', status=404)


def handle403(request, exeption):
    return render(request, '403.html', status=403)


def handle500(request):
    return render(request, '500.html', status=500)
