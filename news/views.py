from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.db.models import Q


def news_home(request):
    search_query = request.GET.get("search", "")

    if search_query:
        news = News.objects.filter(Q(name_news__icontains=search_query)| Q(anons__icontains=search_query))
    else:
        news = News.objects.order_by('-data_create')[:5]

    data = {
        "news": "Новости",
        "all_news": news
    }
    return render(request, "news/news_home.html", data)


class NewsDetailView(DetailView):
    model = News
    template_name = "news/detail-view.html"
    context_object_name = "news"


class NewsUpdate(UpdateView):
    model = News
    template_name = "news/update_news.html"
    form_class = NewsForm


class NewsDelite(DeleteView):
    model = News
    template_name = "news/delite_news.html"
    success_url = "/news"


def create_news(request):
    form = NewsForm()
    data = {
        "create": "Расскажите о новости",
        "form": form,
        "error": "Заполняйте форму правильно!" 
    }

    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main:home")
        else:
            form = NewsForm()
            return render(request, "news/error_add_news.html", {"form": form})
        
    return render(request, "news/create_news.html", data)


