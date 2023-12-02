from .models import Comment
from django import forms
from django.forms import ModelForm
from django.forms.widgets import TextInput

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_content',)
        widgets = {
            'comment_content' : forms.TextInput(attrs={
                'type': 'text',
                'placeholder': 'Write comment here...',
                'name': 'csrfmiddlewaretoken',
                'value': 'ddnPvIJeAs7VT9uIAjHMKH0Vj68RNHSkr5vCd9UScW7s414G3GkMAanheq1aEEvs'
            }),
        }

# class CommentForm(forms.ModelForm):
#     def validate_comment(self):
#         data = self.data['comment_content']
#         if data.length > 500:
#             raise ValidationError(_('Maximum length 500 characters'))
#     class Meta:
#         model = Comment
#         fields = ['comment_content',]
#         help_texts = {'comment_content': ('Enter your comment here.')}

