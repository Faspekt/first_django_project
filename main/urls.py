from django.urls import path, re_path
from . import views

app_name = 'main'

urlpatterns = [
    path("", views.home, name="home"),
    re_path(r"^about", views.about, name="about"),
    re_path(r"^help", views.help, name="help")
]