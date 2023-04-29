from .models import News
from django import forms


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ["name_news", "anons", "full_text", "data_create", "author"]

        widgets = {
            "name_news": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Название"}
            ),
            "anons": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Краткое описание",
                }
            ),
            "full_text": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Полное описание",
                }
            ),
            "data_create": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "hidden"}
            ),
            "author_id": forms.NumberInput(
                attrs={
                    "class": "form-comtrol",
                    "type": "hidden",
                }
            ),
        }
