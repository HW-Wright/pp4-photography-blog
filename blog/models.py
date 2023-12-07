from django.db import models
from django.db.models import Count
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.conf import settings

STATUS = ((False, 'Draft'), (True, 'Published'))

"""Post model for blog posts"""

class Post(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    image = CloudinaryField('image')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='photo_post')
    caption = models.TextField()
    location = models.TextField()
    likes = models.ManyToManyField(User, related_name='photo_likes', blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(choices=STATUS, default=False)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title

    def likes_count(self):
        return self.likes.count()

"""Comment model for user comments"""

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='photo_comment')
    comment_content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_author')
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return f'{self.comment_content} from {self.created_by}'


"""Custom model for mesuring each user's engagement"""

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def user_points(self):
        posts_amount = Post.objects.filter(created_by=self.user).count()
        comments_amount = Comment.objects.filter(created_by=self.user).count()
        points = (posts_amount * 100) + (comment_amount * 50)

        return points


"""Custom model for the site admins"""

class Editor(models.Model):
    name = models.CharField(max_length=50)
    photo = CloudinaryField()
    one_line_bio = models.CharField(max_length=50)

    