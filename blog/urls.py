from . import views
from django.urls import path
from django.conf.urls import handler403, handler404, handler500

urlpatterns = [
    path('', views.FeaturedPosts.as_view(), name='homepage'),
    path('blog', views.AllPosts.as_view(), name='blog'),
    path('like/<slug:slug>', views.LikePost.as_view(), name='post_like'),
    path('add/', views.add_post, name='add'),
    path('edit/<slug:slug>', views.edit_post, name='edit'),
    path('delete_comment/<int:comment_id>/<slug:slug>', views.delete_comment, name='delete_comment'),
    path('delete/<slug:slug>', views.delete_post, name='delete_post'),
    path('specific_post/<slug:slug>', views.SpecificPost.as_view(), name='specific_post')
]

"""Custom Error page handlers"""

handler403 = 'blog.views.handle403'
handler404 = 'blog.views.handle404'
handler500 = 'blog.views.handle500'