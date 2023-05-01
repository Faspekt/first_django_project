from django.db import models
from django.utils import timezone
from django.conf import settings


class News(models.Model):
    name_news = models.CharField("Название", max_length=128)
    anons = models.CharField("Кратное описание", max_length=250)
    full_text = models.TextField("Текст статьи")
    data_create = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, blank=True
    )
    views = models.IntegerField(verbose_name="Кол-во просмотров", default=0)

    def __str__(self):
        return self.name_news

    def get_absolute_url(self):
        return f"/news/{self.id}"

    def save(self, *args, **kwargs):
        if not self.id:
            author = kwargs.get("author", None)
            self.author = author or self.author
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
