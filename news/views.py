import time


from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm
from django.views.generic import DetailView, UpdateView, DeleteView, ListView
from django.db.models import Q
from .services import NewsBD
from django.http import HttpResponse, Http404


class NewsDetailView(DetailView, NewsBD):
    model = News
    template_name = "news/detail-view.html"
    context_object_name = "news_detal"

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        news = News.objects.filter(pk=pk).values(
            "id",
            "name_news",
            "data_create",
            "full_text",
            "views",
            "author__username",
        )

        return news

    def get(self, request, *agrs, **kwargs):
        news = self.get_queryset()
        context = {"news": news}

        if HttpResponse.status_code == 200 and news.exists():
            self.request.session["time_views_update"] = time.time()

            return render(self.request, self.template_name, context)
        else:
            raise Http404


class NewsUpdatePage(UpdateView):
    model = News
    template_name = "news/update_news.html"
    form_class = NewsForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        user = self.request.session.get("user", None)

        if form.is_valid():

            news = form.save(commit=False)
            news.author_id = user.get("id")
            news.published_date = form.cleaned_data["data_create"]
            news.save()

            return redirect("news:news_home")
        else:
            print(form.errors)

        context = {
            "form": form,
        }
        return render(request, self.template_name, context)


class NewsDelite(DeleteView):
    model = News
    template_name = "news/delite_news.html"
    success_url = "/news"


class CreateNews(NewsBD):
    def get(self, request):

        context = {
            "create": "Расскажите о новости",
            "form": NewsForm(),
            "error": "Заполняйте форму правильно!",
        }
        return render(request, self.template_name, context)

    def post(self, request):
        last_operation_time = self.request.session.get("last_operation_time", None)

        return super().create_news(request, last_operation_time)


class NewsPage(ListView, NewsBD):
    model = News
    paginate_by = 5
    template_name = "news/news_home.html"
    context_object_name = "news"

    def get_queryset(self):
        search_query = self.request.GET.get("search", "")
        news_list = self.model.objects.all()

        if search_query:

            news_list = news_list.values(
                "id",
                "name_news",
                "anons",
                "author__username",
            ).filter(
                Q(name_news__icontains=search_query) | Q(anons__icontains=search_query)
            )

        else:
            news_list = news_list.values(
                "id",
                "name_news",
                "anons",
                "author__username",
            ).order_by("-id")

        return news_list

    def post(self, request):
        news_id = self.request.POST.get("id")

        return super().add_views_cache(request, self.model, news_id)
