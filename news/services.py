from time import time


from .forms import NewsForm
from .models import News
from django.shortcuts import redirect
from django.views.generic import View
from django.urls import reverse_lazy


class AddNewsBD(View):
    model = News
    template_name = "news/create_news.html"
    succes_url = reverse_lazy("news:news_home")

    def add_news_to_db(self, request, time_operation):
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
