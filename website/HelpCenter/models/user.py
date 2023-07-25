from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=11, default=True)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def register(self):
        self.save()

    def __str__(self):
        return self.name