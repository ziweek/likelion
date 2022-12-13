from django.db import models


# Create your models here.
#
# class User(models.Model):
#     userid = models.CharField(max_length=16)
#     password = models.CharField(max_length=16)
#     name = models.CharField(max_length=16)
#     major1 = models.ManyToManyField("MajorMain", related_name="users")
#     major2 = models.ManyToManyField("MajorSub", related_name="users")

# class MajorMain(models.Model):
#     major = models.CharField(max_length=16)

# class MajorSub(models.Model):
#     major = models.CharField(max_length=16)


# #
# class Post(models.Model):
#     title = models.TextField(max_length=200)
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
#     content = models.TextField()
#     category = models.ManyToManyField("")

# class Category(models.Model):
#     category = models.CharField(max_length=10)

# class Like(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
#     count = models.IntegerField(default=0)


# #
# class Comment(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
#     comment = models.TextField()

topping_choice = ("양파", "버섯")


class Drink(models.Model):
    name = models.CharField(max_length=10)


class Signature(models.Model):
    name = models.CharField(max_length=10)


class Pizza(models.Model):
    signature = models.OneToOneField(Signature, related_name="pizza")
    toppings = models.CharField(choices=topping_choice)

