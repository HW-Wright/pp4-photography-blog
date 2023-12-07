from django.test import TestCase
from .forms import CommentForm, PostForm, DeleteForm, EditForm

class TestPostForm(TestCase):

    """All posts must be uploaded with a title"""

    def test_title_required(self):
        form = PostForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)

    """All posts must be uploaded with an image file"""

    def test_image_required(self):
        form = PostForm({'image': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)


class TestCommentForm(TestCase):

    """The user cant submit an empty comment"""

    def test_comment_content_required(self):
        form = CommentForm({'coment_content': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('comment_content', form.errors.keys())
        self.assertEqual(
            form.errors['comment_content'][0],
            'This field is required.'
        )


class TestEditForm(TestCase):

    """The user should not be able to alter the slug field from this view"""

    def test_slug_not_present(self):
        form = EditForm()
        self.assertNotIn('slug', form.fields)

    """All posts must be uploaded with a title"""

    def test_title_required(self):
        form = PostForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)
