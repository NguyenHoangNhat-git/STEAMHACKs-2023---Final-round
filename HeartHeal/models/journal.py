from django.db import models

from django.db import models
from .user import User
import datetime

class Note(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Nhật kí của " + self.user.name
    
    def register(self):
        self.save()

    def update(self, new_content):
        self.content = new_content
