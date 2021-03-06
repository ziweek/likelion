from django.shortcuts import render, redirect
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# from django.views.decorators.http import require_POST


def list_page(request):
    """
    1) 모든 Post를 조회한다
    2) 조회한 Post 객체들을 “posts”라는 이름으로 list_page.html에 전달한다.
    """
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "app/list_page.html", context)


# # @require_POST
# def create_page(request):
#     """
#     1) request.method가 POST라면,
#     2) Post 데이터를 생성한다.
#         2-1) 데이터 생성 시, 'title'이라는 이름의 데이터를 꺼내서 title이라는 필드에 넣고,
#         2-2) 'content'라는 이름의 데이터를 꺼내서 content라는 필드에 넣는다.
#     3) 데이터 생성 후에는 'detail_page'라는 이름의 url로 리다이렉트한다.
#     (detail_page로 리다이렉트하기 위해서는 해당 post의 pk값을 적절히 넘겨주어야 하겠죠)
#     """
#     if request.method == 'POST':
#         new_post = Post.objects.create(
#             title=request.POST['title'],
#             content=request.POST['content'],
#         )
#         return redirect('detail_page', new_post.pk)
#     return render(request, 'app/create_page.html')


# def detail_page(request, post_pk):
#     post = Post.objects.get(pk=post_pk)

#     if request.method == "POST":
#         content = request.POST["content"]
#         Comment.objects.create(post=post, content=content)
#         return redirect("detail_page", post_pk)

#     return render(request, "app/detail_page.html", {"post": post})


def edit_page(request, post_pk):
    post = Post.objects.filter(pk=post_pk)
    """
    1) request.method가 POST라면,
    2) post를 수정한다. 
        2-1) 수정 시, 'title'이라는 이름의 데이터를 꺼내서 title이라는 필드에 넣고,
        2-2) 'content'라는 이름의 데이터를 꺼내서 content라는 필드에 넣는다.
    3) 데이터 수정 후에는 'detail_page'라는 이름의 url로 리다이렉트한다.  
        3-1) detail_page로 리다이렉트할 때, 수정한 post 객체의 pk를 넘겨준다.
    """
    if request.method == "POST":
        post.update(title=request.POST["title"], content=request.POST["content"])
        return redirect("detail_page", post_pk)
    return render(request, "app/edit_page.html", {"post": post[0]})


def delete(request, post_pk):
    """
    1) pk가 post_pk인 Post 객체를 조회한다.
    2) 해당 Post 객체를 지운다.
    3) 'list_page'라는 이름의 url로 리다이렉트한다.
    """
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect("list_page")


def delete_comment(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect("detail_page", post_pk)


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        found_user = User.objects.filter(username=username)
        if len(found_user):
            error = "이미 계정이 존재합니다."
            return render(request, "app/signup.html", {"error": error})
        new_user = User.objects.create_user(username=username, password=password)
        auth.login(
            request, new_user, backend="django.contrib.auth.backends.ModelBackend"
        )
        return redirect("list_page")
    return render(request, "app/signup.html")


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(
                request, user, backend="django.contrib.auth.backends.ModelBackend"
            )
            # return redirect('list_page')
            # text = username + "으로 로그인되었습니다."
            # # context = request.GET.get("next", "/")
            # posts = Post.objects.filter(author=username)
            # return render(request, "app/list_page.html", {"text": text, "post": post})
            return redirect(request.GET.get("next", "/"))
        error = "아이디 또는 비밀번호가 틀립니다."
        return render(request, "app/login.html", {"error": error})
    return render(request, "app/login.html")


def logout(request):
    auth.logout(request)
    # return redirect('list_page')
    text = "로그아웃되었습니다."
    return render(request, "app/list_page.html", {"text": text})


@login_required(login_url="/registration/login")
def create_page(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        new_post = Post.objects.create(
            title=title,
            author=request.user,
            content=content,
        )
        return redirect("detail_page", new_post.pk)
    return render(request, "app/create_page.html")


@login_required(login_url="/registration/login")
def detail_page(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    print(type(post.author), "post.author")
    if request.method == "POST":
        content = request.POST["content"]
        Comment.objects.create(
            post=post,
            content=content,
            author=request.user,
        )
        return redirect("detail_page", post_pk)
    return render(request, "app/detail_page.html", {"post": post})


# def detail_page(request, post_pk):
#     post = Post.objects.get(pk=post_pk)

#     if request.method == "POST":
#         content = request.POST["content"]
#         Comment.objects.create(post=post, content=content)
#         return redirect("detail_page", post_pk)

#     return render(request, "app/detail_page.html", {"post": post})
