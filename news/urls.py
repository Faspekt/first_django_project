from django.urls import path, re_path
from . import views

app_name = 'news'

urlpatterns = [
    path("", views.news_home, name="news_home"),
    path("create_news", views.create_news, name="create_news"),
    path("news_check", views.check_user_news, name="check_user_news")
]