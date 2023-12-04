from .models import Comment, Post
from django import forms
from django.forms import ModelForm
from cloudinary.forms import CloudinaryFileField

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_content',)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title', 
            'image',
            'caption',
            'location',
            'status'
            ]
    
    image = CloudinaryFileField()






