from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm
from django.views.generic import DetailView, UpdateView, DeleteView



def news_home(request):
    news = News.objects.order_by('-data_create')[:10]
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



def create_news(request):
    form = NewsForm()
    data = {
        "create": "Расскажите о новости",
        "form": form,
        "error": "Заполняйте форму правильно!" 
    }

    check_user_news(request)
        
    return render(request, "news/create_news.html", data)



def check_user_news(request):

    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main:home")
        else:
            form = NewsForm()
            return render(request, "news/error_add_news.html", {"form": form})


