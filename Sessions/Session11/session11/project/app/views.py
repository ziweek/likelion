# from turtle import title
from django.shortcuts import render, redirect
from .models import Post, Comment

# Create your views here.
from django.contrib.auth.models import User
from django.contrib import auth


def home(request):
    posts = Post.objects.all()

    return render(request, "home.html", {"posts": posts})


def new(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        new_post = Post.objects.create(title=title, content=content)
        return redirect("detail", new_post.pk)

    return render(request, "new.html")


def edit(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        Post.objects.filter(pk=post_pk).update(title=title, content=content)
        return redirect("detail", post_pk)

    return render(request, "edit.html", {"post": post})


def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == "POST":
        content = request.POST["content"]
        Comment.objects.create(post=post, content=content)

        return redirect("detail", post_pk)
    return render(request, "detail.html", {"post": post})


def delete_comment(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect("detail", post_pk)


def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect("home")

def signup(request):
    if request.method =='POST':
        username = request.POST['username']    
        password = request.POST['password']
        found_user = User.objects.filter(username=username)
        if len(found_user):
            error = '이미 아이디가 존재합니다'
            return render(request, 'registration/signup.html', {'error':error})
        new_user = User.objects.create_user(username=username, password=password)
        auth.login(request, new_user) 
        return redirect('home')
    return render(request, 'registration/signup.html')
        