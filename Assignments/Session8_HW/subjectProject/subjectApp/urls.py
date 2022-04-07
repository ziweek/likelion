import imp
from django.contrib import admin
from django.urls import path
from subjectApp import views
from subjectApp.views import AddMajorView, AddSubjectView

app_name = 'subjectApp'

urlpatterns = [
    path('addMajor', AddMajorView.as_view(), name='addMajor'),
    path('addSubject', AddSubjectView.as_view(), name='addSubject'),
    path('', views.home, name='home'),
]