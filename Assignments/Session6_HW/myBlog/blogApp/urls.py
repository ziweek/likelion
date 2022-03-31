from django.urls import path

from . import views

app_name = 'blogApp'

urlpatterns = [
    path('new', views.new, name='new'),
    path('list', views.list, name='list'),
    path('list_detail/<str:article_category>', views.list_detail, name='list_detail'),
    path('detail/<int:article_id>', views.detail, name='detail'),
]