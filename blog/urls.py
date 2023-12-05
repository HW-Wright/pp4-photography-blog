from . import views
from django.urls import path

urlpatterns = [
    path('', views.FeaturedPosts.as_view(), name='homepage'),
    path('blog', views.AllPosts.as_view(), name='blog'),
    path('like/<slug:slug>', views.LikePost.as_view(), name='post_like'),
    path('add/', views.add_post, name='add'),
    path('edit/<slug:slug>', views.edit_post, name='edit'),
    path('<comment_id>', views.delete_comment, name='delete_comment'),
    path('<slug:slug>', views.delete_post, name='delete_post'),
    path('specific_post/<slug:slug>', views.SpecificPost.as_view(), name='specific_post')
]