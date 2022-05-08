from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy

# Create your views here.
from .models import Major, Subject
from .forms import MajorModelForm, SubjectModelForm


class AddMajorView(CreateView):
    model = Major
    form_class = MajorModelForm
    template_name = 'addMajor.html'
    success_url = reverse_lazy('home')


class AddSubjectView(CreateView):
    model = Subject
    form_class = SubjectModelForm
    template_name = 'addSubject.html'
    success_url = reverse_lazy('home')


class EditMajorView(UpdateView):
    model = Major
    form_class = MajorModelForm
    template_name = 'editMajor.html'
    success_url = reverse_lazy('home')


class EditSubjectView(UpdateView):
    model = Subject
    form_class = SubjectModelForm
    template_name = 'editSubject.html'
    success_url = reverse_lazy('home')


def home(request):
    majors = Major.objects.all()
    subjects = Subject.objects.all()
    context = {'majors': majors, 'subjects': subjects}
    return render(request, 'home.html', context)


def deleteMajorView(request, major_pk):
    target_major = Major.objects.get(pk=major_pk)
    target_major.delete()
    return redirect('home')


def deleteSubjectView(request, subject_pk):
    target_subject = Subject.objects.get(pk=subject_pk)
    target_subject.delete()
    return redirect('home')

def businsessView(request):
    subjects = Subject.objects.all()
    target_major = subjects.filter(major__name='경영학과')
    context = {'target_major': target_major}
    return render(request, 'business.html', context)
