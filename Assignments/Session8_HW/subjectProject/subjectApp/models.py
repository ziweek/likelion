from django.db import models

# Create your models here.
class Major(models.Model):
    name = models.TextField(max_length=200)

    def __str__(self):
        return self.name


class Subject(models.Model):
    major = models.TextField(max_length=200)
    subject_name = models.TextField(max_length=200)
    prof_name = models.TextField(max_length=200)
    memo = models.TextField(max_length=200)

    def __str__(self):
        return self.name