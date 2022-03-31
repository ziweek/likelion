from django.shortcuts import render, redirect

# Create your views here.
from .models import Article

def new(request):
    if request.method == 'POST':
        print(request.POST)
        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content']
        )
        return redirect('blogProject:list')
    return render(request, 'blogProject/new.html')

def list(request):
    articles = Article.objects.all()
    context = {'articles' : articles}
    return render(request, 'blogProject/list.html', context)

def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    context = {'article' : article}
    return render(request, 'blogProject/detail.html', context)