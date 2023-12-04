from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm, PostForm
from django.contrib.messages.views import SuccessMessageMixin


class FeaturedPosts(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=True).order_by('-date_created')[:3]
    template_name = 'index.html'


# def add_post(request):
#     if request.method == 'POST':
#         post_form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = post_form.save(commit=False)
#             post.created_by = request.user
#             form.save()
#             return redirect('index.html')
#         else:
#             post_form = PostForm(request.POST, request.FILES)
    
#     return render()


class AddPost(SuccessMessageMixin, generic.CreateView):

    model = Post
    template_name = 'add_post.html'
    form_class = PostForm
    success_message = 'Congratulations! Post added!'

    def form_valid(self, form):
        form = PostForm(request.POST, request.FILES)
        form.instance.author = self.request.user
        return super().form_valid(form)

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

