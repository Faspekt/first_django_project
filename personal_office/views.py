import os

from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView, UpdateView
from django.urls import reverse_lazy

from .forms import AvatarUploadForm
from .services import StatistiNews
from users.models import User
from news.models import News
from users.services import Avatar


class PersonalOfficePage(ListView):
    template_name = "personal_office/personal_office.html"

    def get(self, request, *args, **kwargs):
        try:
            user = self.request.session.get("user")
        except KeyError:
            return HttpResponse(
                "<h1>Зарегестирируйтесь для тего чтобы добовлять новости</h1>"
            )

        return render(request, "personal_office/personal_office.html", user)


class HistoryNewsPage(ListView):
    context_object_name = "history_news_user"
    template_name = "personal_office/history_news_added_by_user.html"
    model = News
    paginate_by = 5

    def get_queryset(self):
        user = self.request.session.get("user")
        user_uploaded_news = self.model.objects.filter(author_id=user.get("id")).values(
            "id", "name_news", "anons"
        )

        return user_uploaded_news


class StatisticNewsPage(StatistiNews):
    model = News
    template_name = "personal_office/statistic_news.html"

    def get(self, request, pk):
        coutn_news = super().count_news_from_user(self.model, pk)

        return render(request, self.template_name, context={"coutn_news": coutn_news})


class AvatarUpdate(UpdateView, Avatar):
    model = User
    template_name = "personal_office/change_avatar.html"
    form_class = AvatarUploadForm
    success_url = reverse_lazy("main:home")

    def post(self, request, pk: int) -> HttpResponse:
        form = AvatarUploadForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save(commit=False)
            user.id = pk
            user.avatar = form.cleaned_data["avatar"]
            user.save(update_fields=["avatar"])

            path_image = os.path.join("media", str(user.avatar))
            # user.avatar.url does not fit here

            path_convert_image = super().convert_image(request, path_image, user_id=pk)

            user.avatar = str(path_convert_image)
            user.save(update_fields=["avatar"])

            user = self.request.session.get("user")
            user["avatar"] = request.user.avatar.url
            self.request.session["user"] = user

        return redirect(self.success_url)
