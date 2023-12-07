from django.test import TestCase
from django.urls import reverse
from .models import User, Post, Comment, Editor
from .views import FeaturedPosts, SpecificPost, LikePost, edit_post, add_post,
delete_post


class TestViews(TestCase):

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

    """The view should produce the three posts with the most likes,
    and render them in index.html.
    """

    def test_get_featured_posts(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    """The view should select the slug for the requested post and render
    specific_post.html
    """

    def test_get_specific_post(self):
        response = self.client.get(
            reverse('specific_post', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'specific_post.html')

    """This new should redirect the user to the edit_post template"""

    def test_edit_post(self):
        response = self.client.get(reverse('edit', args=[self.post.slug]))
        self.assertEqual(response.status_code, 302)

    """This view should redirect the user to the add_post template"""

    def test_add_post(self):
        response = self.client.get(reverse('add'))
        self.assertEqual(response.status_code, 302)

    """This view should redirect the user to the
    delete post form on delete_post.html"""

    def test_delete_post(self):
        response = self.client.get(
            reverse('delete_post', args=[self.post.slug]))
        self.assertEqual(response.status_code, 302)
