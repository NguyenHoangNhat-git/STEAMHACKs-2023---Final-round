from django.db import models

from .user import User

from ckeditor.fields import RichTextField

import datetime

class Practice_Category(models.Model):
    name = models.CharField(max_length=100)

    def  __str__(self):
        return self.name

class Practice(models.Model):
    title = models.CharField(max_length=60)
    category = models.ForeignKey(Practice_Category, blank=True, null=True, on_delete=models.SET_NULL)
    description = models.TextField()
    content_overview = models.TextField(blank=True, null=True)
    duration = models.CharField(max_length=50)

    image = models.ImageField(upload_to='imgs/', blank=True)

    by = models.CharField(max_length=200, blank=True, null=True)

    timestamp = models.DateField(default=datetime.date.today())

    def  __str__(self):
        return self.title

class What_yll_learn(models.Model):
    practice = models.ForeignKey(Practice, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)

    def  __str__(self):
        return self.content


class Module(models.Model):
    title = models.CharField(max_length=60)
    practice = models.ForeignKey(Practice, on_delete=models.CASCADE)
    duration = models.CharField(max_length=50)

    overview = models.TextField(null=True, blank=True)

    content = RichTextField(null=True, blank=True)
    video = models.FileField(upload_to='video/', null=True, blank=True)
    video_link = models.TextField(null=True, blank=True)

    def  __str__(self):
        return self.title


class Module_user(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)

    done = models.BooleanField(default=False)

    def __str__(self):
        return "Bài tập của" + self.user.name + " về : " + self.module.title

def get_modules_user(current_user, practice):
    return Module_user.objects.filter(user=current_user, practice=practice)