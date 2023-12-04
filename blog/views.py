from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import CommentForm, PostForm, EditForm
from django.contrib.messages.views import SuccessMessageMixin


class FeaturedPosts(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=True).order_by('-date_created')[:3]
    template_name = 'index.html'


class EditComment(generic.UpdateView):
    model = Comment
    template_name = 'edit_comment.html'
    form_class = CommentForm

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=True)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.photo_comment.order_by("date_created")
        liked = False
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

        return render(
            request,
            "specific_post.html",
            {
                "post": post,
                "comments": comments,
                "comment_form": CommentForm(),
                "liked": liked
            },
        )

class SpecificPost(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=True)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.photo_comment.order_by("date_created")
        print(CommentForm())
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

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=True)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.photo_comment.order_by("date_created")
        liked = False
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

        return render(
            request,
            "specific_post.html",
            {
                "post": post,
                "comments": comments,
                "comment_form": CommentForm(),
                "liked": liked
            },
        )


class LikePost(View):

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


def add_post(request):
    form = PostForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            new_post = form.save(commit=False)
            post.created_by = request.user
            new_post = form.save()
            return redirect('index.html')
        else:
            form = PostForm(request.POST, request.FILES)
    
    context = {
        'form': form
    }

    return render(request, 'add_post.html', context)


def delete_post(request, slug):
    queryset = Post.objects.filter(status=True).order_by('-date_created')
    post = get_object_or_404(queryset, slug=slug)
    if request.user == Post.created_by:
        post.delete()

    context = {
        'queryset': queryset
    }
    return render(request, 'blog.html', context)






# def edit_comment(request, slug, comment_id):
#     queryset = Post.objects.all
#     comment = get_object_or_404(Comment, slug=slug, id=comment_id)
#     if request.user == Comment.created_by:
#         return redirect('edit_comment.html')
#     if request.method == 'POST':
#         form = CommentForm(request.POST, instance=comment)
#         if form.is_valid():
#             form.save()
#             return redirect('specific_post.html', slug=slug)
#     else:
#         form = CommentForm(instance=comment)
    
#     context = {
#         'form': form,
#         'comment': comment
#     }

#     return render(request, 'edit_comment.html', context)
 
#     return redirect('specific_post.html', slug)


