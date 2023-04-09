from .models import News
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput
from django.utils import timezone


class NewsForm(ModelForm):
    class Meta:
          model = News
          fields = ["name_news", "anons", "full_text", "data_create"]


          widgets = {
               "name_news": TextInput(attrs={
                    "class": "form-control",
                    "placeholder": "Название"
           }),
               "anons": TextInput(attrs={
                    "class": "form-control",
                    "placeholder": "Краткое описание"
           }),
               "full_text": Textarea(attrs={
                    "class": "form-control",
                    "placeholder": "Полное описание"
           }),
               "data_create": DateTimeInput(attrs={
                    "class": "form-control",
                    "type": "hidden"
               })
        }

