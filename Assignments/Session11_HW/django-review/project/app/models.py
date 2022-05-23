from operator import mod
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=50, null=True)
    content = models.TextField(null=True)
    author = models.ForeignKey(User, models.CASCADE, related_name="posts")

    def __str__(self):
        return str(self.title)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    author = models.ForeignKey(User, models.CASCADE, related_name="comments")

    def __str__(self):
        return str(self.content)
