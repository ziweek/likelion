from unicodedata import name
from django.urls import path

from . import views

app_name = 'listApp'

urlpatterns = [
    path('list', views.list, name='list'),
    path('new', views.new, name='new'),
    path('detail/<int:todo_id>', views.detail, name='detail'),
    path('edit/<int:todo_id>', views.edit, name='edit'),
    path('delete/<int:todo_id>', views.delete, name='delete')
]