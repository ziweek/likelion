from unicodedata import category
from django.shortcuts import render, redirect

# Create your views here.
from .models import Ariticle
from datetime import datetime

def new(request):
    if request.method == 'POST':
        print(request.POST)
        new_article = Ariticle.objects.create(
            title = request.POST['title'],
            category = request.POST['category'],
            post_time = datetime.now(),
            content = request.POST['content']
        )
        return redirect('blogApp:list')
    return render(request, 'blogApp/new.html')

def list(request):
    articles = Ariticle.objects.all()
    categoties_hobby = Ariticle.objects.filter(category = 'hobby')
    categoties_food = Ariticle.objects.filter(category = 'food')
    categoties_programming = Ariticle.objects.filter(category = 'programming')
    context = {
        'num_categoties_hobby':len(categoties_hobby),
        'num_categoties_food':len(categoties_food),
        'num_categoties_programming':len(categoties_programming)
        }
    return render(request, 'blogApp/list.html', context)

def list_detail(reqeust, article_category):
    articles_filtered = Ariticle.objects.filter(category=article_category)
    context = {'articles_filtered':articles_filtered}
    return render(reqeust, 'blogApp/list_detail.html', context)

def detail(request, article_id):
    article = Ariticle.objects.get(id=article_id)
    context = {'article':article}
    return render(request, 'blogApp/detail.html', context)