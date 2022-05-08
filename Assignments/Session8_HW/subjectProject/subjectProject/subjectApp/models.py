from django.db import models

# Create your models here.
class Major(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)


class Subject(models.Model):
    name = models.CharField(max_length=200)
    major = models.ForeignKey('Major', on_delete=models.CASCADE, related_name='subject')
    prof_name = models.CharField(max_length=200)
    memo = models.TextField()

    def __str__(self):
        return str(self.name)