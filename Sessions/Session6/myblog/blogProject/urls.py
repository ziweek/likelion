from django.urls import path

from . import views

app_name = 'blogProject'

urlpatterns = [
    path('new', views.new, name='new'),
    path('list', views.list, name='list'),
    path('detail/<int:article_id>', views.detail, name='detail')
]