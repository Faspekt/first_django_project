from django.views.generic import ListView


class StatistiNews(ListView):

    def count_news_from_user(self, model, pk):
        count_news = self.model.objects.filter(author_id=pk).values("id").count()

        return count_news
