from django.urls import path

from . import views

app_name = 'app'

urlpatterns = [
    path('', views.list, name='list'),
    # path('list', views.list, name='list'),
    # path('new', views.new, name='new'),
    # path('detail/<int:post_id>', views.detail, name='detail'),
]