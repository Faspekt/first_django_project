from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from news.models import News
from .services import StatistiNews


class PersonalOfficePage(ListView):
    template_name = "personal_office/personal_office.html"

    def get(self, request, *args, **kwargs):
        try:
            user = self.request.session.get("user")
        except KeyError:
            return HttpResponse("<h1>Зарегестирируйтесь для тего чтобы добовлять новости</h1>")

        return render(request, "personal_office/personal_office.html", user)


class HistoryNewsPage(ListView):
    context_object_name = "history_news_user"
    template_name = "personal_office/history_news_added_by_user.html"
    model = News
    paginate_by = 5

    def get_queryset(self):
        user = self.request.session.get("user")
        user_uploaded_news = self.model.objects.filter(author_id=user.get("id")).values("id", "name_news", "anons")

        return user_uploaded_news


class StatisticNewsPage(StatistiNews):
    model = News
    template_name = "personal_office/statistic_news.html"

    def get(self, request, pk):
        coutn_news = super().count_news_from_user(self.model, pk)

        return render(request, self.template_name, context={"coutn_news": coutn_news})
