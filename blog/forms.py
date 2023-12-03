from .models import Comment
from django import forms
from django.forms import ModelForm
from django.forms.widgets import TextInput

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_content',)



