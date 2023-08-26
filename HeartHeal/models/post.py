from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone

import datetime

from .user import User

class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='imgs/', blank=True)
    content = models.TextField(blank=True)
    categories = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)

    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name + " đăng : " + self.title
    
    def get_all_posts():
        return Post.objects.all()


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name + " thích bài viết : " + self.post.__str__()


class Comment(models.Model):    
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return "Bình luận của " + self.user.name + " vào lúc " + timezone.localtime(self.timestamp).strftime("%H:%M:%S %d/%m/%Y")


def get_comment_num_func(self):
    all_comments = Comment.objects.filter(post=self)
    comment_num = 0
    for comment in all_comments:
        comment_num += 1
    return comment_num


def get_like_num_func(self):
    all_likes = Like.objects.filter(post=self)
    like_num = 0
    for like in all_likes:
        like_num += 1
    return like_num

def get_all_comment_func(self):
    return Comment.objects.filter(post=self)

def if_current_user_liked_func(self, user_id):
    current_user = User.get_user_by_id(user_id)
    if_like = Like.objects.filter(post=self, user=current_user)
    return if_like.exists()


Post.get_comment_num = get_comment_num_func
Post.get_like_num = get_like_num_func
Post.get_all_comment = get_all_comment_func
Post.if_current_user_liked = if_current_user_liked_func