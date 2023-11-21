from . import views
from django.urls import path

urlpatterns = [
    path('', views.FeaturedPosts.as_view(), name='home')
]