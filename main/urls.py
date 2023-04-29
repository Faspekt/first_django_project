from django.urls import path, re_path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.HomePage.as_view(), name="home"),
    re_path(r"^about_page", views.about_page, name="about"),
    re_path(r"^help_page", views.help_page, name="help"),
]
