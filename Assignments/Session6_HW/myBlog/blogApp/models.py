from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=10)
    address = models.TextField()

class Ariticle(models.Model):
    hobby = 'hb'
    food = 'fd'
    programming = 'pg'
    category_choice = [
        (hobby,'hobby'),
        (food,'food'),
        (programming,'programming'),
    ]
    title = models.CharField(max_length=100)
    category = models.CharField(choices=category_choice, max_length=2, blank=True)
    post_time = models.TimeField()
    content = models.TextField()

    def __str__(self):
        return self.title