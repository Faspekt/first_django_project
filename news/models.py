from django.db import models
from django.utils import timezone
from users.models import User


class News(models.Model):

    
    name_news = models.CharField("Название", max_length=128)
    anons = models.CharField("Кратное описание", max_length=250)
    full_text = models.TextField("Текст статьи")
    data_create = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True)

    def __str__(self):
        return self.name_news
    
    def get_absolute_url(self):
        return f"/news/{self.id}"

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
    