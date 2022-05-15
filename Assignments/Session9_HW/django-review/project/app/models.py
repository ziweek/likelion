from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50, null=True)
    content = models.TextField(null=True)

    def __str__(self):
        return str(self.title)
