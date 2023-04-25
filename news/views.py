from django.shortcuts import render
from .models import News
from .forms import NewsForm
from django.views.generic import DetailView, UpdateView, DeleteView, ListView
from django.db.models import Q
from .services import AddNewsBD


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


class CreateNews(AddNewsBD):
    def get(self, request):
        context = {
            "create": "Расскажите о новости",
            "form": NewsForm(),
            "error": "Заполняйте форму правильно!",
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        return super().add_news_to_db(request)
    

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
