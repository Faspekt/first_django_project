from django.urls import path
from . import views


app_name = "personal_office"

urlpatterns = [
    path("<int:pk>", views.PersonalOfficePage.as_view(), name="personal_office_page"),
    path("<int:pk>/histiry_news", views.HistoryNewsPage.as_view(), name="history_news")
]