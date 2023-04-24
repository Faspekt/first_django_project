from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm
from django.views.generic import DetailView, UpdateView, DeleteView, ListView
from django.db.models import Q
from users.models import User



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
        "error": "Заполняйте форму правильно!",

    }

    if request.method == "POST":
        form = NewsForm(request.POST)
        
        if form.is_valid():

            name_news = form.cleaned_data["name_news"]
            anons = form.cleaned_data["anons"]
            full_text = form.cleaned_data["full_text"]
            data_create = form.cleaned_data["data_create"]
            author = request.user.id

            News.objects.create(
                name_news = name_news,
                anons = anons,
                full_text = full_text,
                data_create = data_create,
                author_id = author
            )
            return redirect("main:home")
        else:
            form = NewsForm()
            return render(request, "news/error_add_news.html", {"form": form})
        
    return render(request, "news/create_news.html", data)


class NewsPage(ListView):
    model = News
    paginate_by = 5
    template_name = "news/news_home.html"
    context_object_name = 'news'
    
    def get_queryset(self):
        search_query = self.request.GET.get("search", "")
        news_list = self.model.objects.all()
        if search_query:
            news_list = news_list.filter(Q(name_news__icontains=search_query)| Q(anons__icontains=search_query))
        else:
            news_list = news_list.order_by('-id')
        
        return news_list
