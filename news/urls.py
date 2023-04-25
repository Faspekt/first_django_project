from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path("",views.NewsPage.as_view(), name="news_home"),
    path("create_news", views.CreateNews.as_view(), name="create_news"),
    path("<int:pk>", views.NewsDetailView.as_view(), name="news-detail-view"),
    path("<int:pk>/update", views.NewsUpdate.as_view(), name="news_update"),
    path("<int:pk>/delite", views.NewsDelite.as_view(), name="news_delite"),
]
