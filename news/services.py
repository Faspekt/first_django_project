from .forms import NewsForm
from .models import News
from django.shortcuts import render, redirect
from django.views.generic import View
from django.urls import reverse_lazy
from django.shortcuts import render





class AddNewsBD(View):


    def __init__(self, model=News, template_name="news/create_news.html", succes_url=reverse_lazy("news:news_home")) -> None:
        self.model = model
        self.template_name = template_name
        self.succes_url = succes_url
        

    def add_news_to_db(self, request):
        form = NewsForm(request.POST)

        if form.is_valid():
            name_news = form.cleaned_data["name_news"]
            anons = form.cleaned_data["anons"]
            full_text = form.cleaned_data["full_text"]
            data_create = form.cleaned_data["data_create"]
            author = self.request.user.id

            News.objects.create(
                name_news = name_news,
                anons = anons,
                full_text = full_text,
                data_create = data_create,
                author_id = author
            )
            return redirect(self.succes_url)
        
        context = {
            "create": "Расскажите о новости",
            "form": form,
            "error": "Заполняйте форму правильно!",
        }

        return render(request, self.template_name, context)
    
