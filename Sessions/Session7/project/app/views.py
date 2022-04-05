from django.shortcuts import render

# Create your views here.
def list(request):
    context = {:,:}
    return render(request, '', context)

def new(request):
    return 0

def detail(request):
    return 0