from unicodedata import name
from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=10)
    address = models.TextField()

class Category(models.Model):
    name = models.CharField(max_length=10)
    description = models.TextField()

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title