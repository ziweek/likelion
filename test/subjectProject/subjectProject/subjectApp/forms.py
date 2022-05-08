from dataclasses import fields
from django import forms

from .models import Major, Subject


major_choices = Major.objects.all().values_list('name', 'name')


class MajorModelForm(forms.ModelForm):
    class Meta:
        model = Major
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '전공명을 입력하세요.'})
        }


class SubjectModelForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ('name', 'major', 'prof_name', 'memo')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '과목명을 입력하세요.'}),
            'major': forms.Select(choices=major_choices, attrs={'class': 'form-control'}),
            'prof_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '교수님을 입력하세요.'}),
            'memo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '메모를 입력하세요.'}),
        }
