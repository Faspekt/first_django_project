from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path("", views.news_home, name="news_home"),
    path("create_news", views.create_news, name="create_news"),
    path("news_check", views.check_user_news, name="check_user_news"),
    path("<int:pk>", views.NewsDetailView.as_view(), name="news-detail-view"),
    path("<int:pk>/update", views.NewsUpdate.as_view(), name="news_update")
]