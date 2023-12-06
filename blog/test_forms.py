from django.test import TestCase
from .form import CommentForm, PostForm, DeleteForm, EditForm

class TestPostForm(TestCase):

    def test_title_required(self):
        form = PostForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)

    def test_image_required(self):
        form = PostForm({'image': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)
    
    def


# class TestCommentForm(TestCase):
    

# class TestDeleteForm(TestCase):
    

# class TestEditForm(TestCase):
    