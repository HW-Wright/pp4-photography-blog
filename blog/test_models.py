from django.test import TestCase
from .models import Post, User, Comment

class TestModels(TestCase):

    """Test data"""
    @classmethod
    def setUpTestData(self):
        self.user = User.objects.create(username='testuser')
        self.user.set_password('welcome1')
        self.user.save()

        self.post = Post.objects.create(
            title='test',
            image='img.jpeg',
            slug='test',
            created_by=self.user,
            status=True
        )
        self.post.save()

        self.comment = Comment.objects.create(
            post=self.post,
            created_by=self.user,
            comment_content='test',
        )

    """All New posts should have a slug that matches thier title"""

    def test_post_slug_matches_title(self):
        self.assertEqual(self.post.title, self.post.slug)

    """Each new comment must accuratley reflect the user author"""

    def test_comment_created_by_equals_user(self):
        self.assertEqual(self.comment.created_by, self.user)
