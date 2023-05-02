from time import time

from .forms import NewsForm
from .models import News
from django.shortcuts import redirect
from django.views.generic import View
from django.urls import reverse_lazy
from django.core.cache import cache


class NewsBD(View):
    model = News
    template_name = "news/create_news.html"
    succes_url = reverse_lazy("news:news_home")

    def create_news(self, request, time_operation):
        form = NewsForm(request.POST)
        user = self.request.session.get("user")
        time_now = time()

        if time_operation is None or time_now - time_operation > 60:
            if form.is_valid():
                name_news = form.cleaned_data["name_news"]
                anons = form.cleaned_data["anons"]
                full_text = form.cleaned_data["full_text"]
                data_create = form.cleaned_data["data_create"]
                author = user.get("id")

                News.objects.create(
                    name_news=name_news,
                    anons=anons,
                    full_text=full_text,
                    data_create=data_create,
                    author_id=author,
                )
                self.request.session["last_operation_time"] = time_now
                return redirect(self.succes_url)
        else:
            return redirect("main:home")

    def add_views_cache(self, request, model, news_id):
        # add views on 1 in cache, if user was on page more 5 minuts

        time_views_update = self.request.session.get("time_views_update", None)

        if (time() - time_views_update) > 300:
            key = f"{news_id}"

            views_count = cache.get(key)

            if views_count is None:
                views_count = model.objects.filter(id=news_id).values_list("views", flat=True)[0]
                cache.set(key, views_count + 1, 600)

            else:
                cache.set(key, views_count + 1)

            return redirect(self.succes_url)

        else:
            return redirect(self.succes_url)

    def add_views_to_db(self, key: str):
        views_news = cache.get(key)

        if views_news is not None:
            try:
                self.model.objects.filter(id=key).update(views=views_news)

            except News.DoesNotExist:
                pass
        else:
            pass
