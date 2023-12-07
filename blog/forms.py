from .models import Comment, Post
from django import forms
from django.forms import ModelForm
from django.utils.text import slugify
from cloudinary.forms import CloudinaryFileField
from crispy_forms.helper import FormHelper

"""Form to add a comment"""

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_content',)

"""Form to add a post"""

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

"""Form to remove a post"""

class DeleteForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = []

"""Form to amend a post"""

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'caption',
            'location',
            'status'
            ]






