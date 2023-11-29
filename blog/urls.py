from . import views
from django.urls import path

urlpatterns = [
    path('', views.FeaturedPosts.as_view(), name='homepage'),
    path('blog', views.AllPosts.as_view(), name='blog'),
    path('<slug:slug>/', views.SpecificPost.as_view(), name='specific_post'),
]