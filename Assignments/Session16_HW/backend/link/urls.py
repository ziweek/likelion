from django.contrib import admin
from django.urls import path

from .views import redirect

app_name = 'link'

urlpatterns = [
    path('redirect', redirect, name='redirect')
]
