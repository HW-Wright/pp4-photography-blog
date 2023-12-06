from django.contrib import admin
from .models import Post, Comment, Editor, UserProfile
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug' : ('title',)}
    list_filter = ('status', 'date_created')
    list_display = ('title', 'status', 'date_created')
    search_fields = ('title', 'status')
    summernote_fields = ('caption')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('post', 'created_by', 'comment_content', 'date_created')
    list_filter = ('post', 'date_created')
    search_fields = ('post', 'created_by')