from django.contrib import admin
from django.urls import path

from .views import signup

app_name = 'login'

urlpatterns = [
    path('', signup, name='login')
]
