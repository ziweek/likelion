from django.shortcuts import render, redirect

# Create your views here.
def redirect(request):
    if True:
        return redirect('https://ziweek.github.io/starwars_game/#intro')
    return render(request, 'login/index.html')