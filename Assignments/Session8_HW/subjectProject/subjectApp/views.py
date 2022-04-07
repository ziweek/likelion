from django.shortcuts import render, redirect

# Create your views here.
from .models import Major, Subject
from django.views.generic import CreateView, UpdateView
from .forms import MajorModelForm, SubjectModelForm
from django.urls import reverse_lazy

class AddMajorView(CreateView):
    model = Major
    form_class = MajorModelForm
    template_name = 'subjectApp/addMajor.html'
    success_url = reverse_lazy('home')

class AddSubjectView(CreateView):
    model = Subject
    form_class = SubjectModelForm
    template_name = 'subjectApp/addSubject.html'
    success_url = reverse_lazy('home')

def home(request):
    if request == 'POST':
        new_major = Major.objects.create(
            name = request.POST['name']
        )
        return redirect('subjectApp:home')
    majors = Major.objects.all()
    context = {'majors':majors}
    return render(request, 'subjectApp/home.html',context)