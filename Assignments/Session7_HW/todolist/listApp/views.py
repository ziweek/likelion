from django.shortcuts import render, redirect
from matplotlib.pyplot import title

# Create your views here.
from .models import Todo
from datetime import datetime

def list(request):
    todos = Todo.objects.all()
    context = {'todos':todos}
    return render(request, 'listApp/list.html', context)

def new(request):
    if request.method == 'POST':
        print(request.method)
        new_todo = Todo.objects.create(
            title = request.POST['title'],
            date = request.POST['date'],
            content = request.POST['content'],
        )
        return redirect('listApp:list')
    return render(request, 'listApp/new.html')

def detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    context = {'todo':todo}
    return render(request, 'listApp/detail.html', context)

def edit(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    context = {'todo':todo}
    if request.method == 'POST':
        Todo.objects.filter(id=todo_id).update(
            title = request.POST['title'],
            date = request.POST['date'],
            content = request.POST['content']
        )
        return redirect('listApp:detail', todo_id)
    return render(request, 'listApp/edit.html', context)

def delete(request, todo_id):
    post = Todo.objects.get(id=todo_id)
    post.delete()
    return redirect('listApp:list')