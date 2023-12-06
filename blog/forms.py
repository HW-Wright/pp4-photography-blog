from .models import Comment, Post
from django import forms
from django.forms import ModelForm
from django.utils.text import slugify
from cloudinary.forms import CloudinaryFileField
from crispy_forms.helper import FormHelper


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


class DeleteForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = []


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'caption',
            'location',
            'status'
            ]






