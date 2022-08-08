from django.urls import path
from account import views

app_name = "account"
urlpatterns = [
    # /accounts/
    path("", views.home, name="home"),
    path("signup", views.signup, name="signup"),
]
