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
    
    # def __init__(self, *args, **kwargs):
    #     super(PostForm, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper(self)

    # def save(self, *args, **kwargs):
    #     self.instance.slug = slugify(self.cleaned_data['title]'])
    #     return super(PostForm, self).save(*args, **kwargs)


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'caption',
            'location',
            'status'
            ]






