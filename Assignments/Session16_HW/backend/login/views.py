from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.
# def init(request):
#     return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        new_uwer = User.objects.create_user(username=username, password=password)
        return redirect('https://ziweek.github.io/starwars_game/#intro')
    return render(request, 'index.html')