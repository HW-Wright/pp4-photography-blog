from . import views
from django.urls import path

urlpatterns = [
    path('', views.FeaturedPosts.as_view(), name='homepage'),
    path('blog', views.AllPosts.as_view(), name='blog'),
    path('like/<slug:slug>', views.LikePost.as_view(), name='post_like'),
    path('add/', views.add_post, name='add'),
    path('edit/<slug:slug>', views.edit_post, name='edit'),
    path('edit_comment', views.EditComment.as_view(), name='edit_comment'),
    path('delete/<slug:slug>', views.delete_post, name='delete_post'),
    path('specific-post/<slug:slug>/', views.SpecificPost.as_view(), name='specific_post')
]