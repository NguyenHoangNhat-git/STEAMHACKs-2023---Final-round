from django.db import models
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='imgs/', blank=True)
    slug = models.TextField(blank=True)
    content = RichTextField()


    def __str__(self):
        return self.title

